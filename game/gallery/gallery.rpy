#########
# Gallery
#
# Supplies a gallery for those post-game image collectors / reviewers.
#########

# TODO: find a way to use edgescrolls instead of transforms (seems to be a gallery limitation)
# TODO: add some additional filters / sort options

transform gallery_scroll_x:
     yalign 0.5
     xalign 1.0
     linear 5.0 xalign 0.0
     linear 5.0 xalign 1.0
     linear 2.5 xalign 0.5
     function gallery.transform_zoom

transform gallery_scroll_y:
     xalign 0.5
     yalign 1.0
     linear 5.0 yalign 0.0
     linear 5.0 yalign 1.0
     linear 2.5 yalign 0.5
     function gallery.transform_zoom

transform gallery_instant_zoom:
     xalign 0.5
     yalign 0.5
     function gallery.transform_instant_zoom


init python:

    #define styles (for some reason we have to do it in python code)
    style.gallery_menu_style = Style(style.default)
    style.gallery_menu_style.clear()
    style.gallery_stats_text_style = Style(style.default)
    style.gallery_stats_text_style.outlines = [(1, '#000000', 0, 0),(2, '#808080', 0, 0)]

    class GalleryManager(object):

        class ShowMenu(ShowMenu):
            """ Action to show the gallery
            """

            def __init__(self, screen='gallery', transition=None, speed=0.5):
                if transition is None:
                    transition = Dissolve(speed)
                self.transition = transition
                super(GalleryManager.ShowMenu, self).__init__(screen=screen)

            def __call__(self):
                """ ShowMenu action override """
                #NOTE: it doesn't call it's super, so neither will we

                if not self.get_sensitive():
                    return

                #preload the gallery
                gallery.preload_images()

                orig_screen = screen = self.screen or store._game_menu_screen

                if not (renpy.has_screen(screen) or renpy.has_label(screen)):
                    screen = screen + "_screen"

                # They consider this ugly, so it may change at some point
                if renpy.context()._menu:
                    if renpy.has_screen(screen):
                        renpy.transition(self.transition)
                        renpy.show_screen(screen, _transient=True)
                        renpy.restart_interaction()
                    elif renpy.has_label(screen):
                        renpy.transition(self.transition)
                        ui.layer("screens")
                        ui.remove_above(None)
                        ui.close()
                        renpy.jump(screen)
                    else:
                        raise Exception("%r is not a screen or a label." % orig_screen)
                else:
                    renpy.call_in_new_context("_game_menu", _game_menu_screen=screen)

        def transform_zoom(self, trans, st, at):
            #we can't let them edgescroll, so we might as well zoom out
            win_size = (config.screen_width, config.screen_height)
            img_size = self.get_image_size(trans.child.target.filename)
            z_scale = min(float(win_size[0]) / img_size[0], float(win_size[1]) / img_size[1])
            z_time = 5.0
            if st > z_time:
                trans.zoom = z_scale
                return None
            else:
                trans.zoom = 1.0 - ((1 - z_scale) * st / z_time)
                return 0

        def transform_instant_zoom(self, trans, st, at):
            #we can't let them edgescroll, so we might as well zoom out
            win_size = (config.screen_width, config.screen_height)
            img_size = self.get_image_size(trans.child.target.filename)
            z_scale = min(float(win_size[0]) / img_size[0], float(win_size[1]) / img_size[1])
            trans.zoom = z_scale
            return None

        def base_button(self, text, action=None, scale=1, xpos=None, ypos=None, reverse=False, **kwargs):
            if reverse:
                idle_image = 'images/ui/main_hover.png'
                hover_image = 'images/ui/main_idle.png'
            else:
                idle_image = 'images/ui/main_idle.png'
                hover_image = 'images/ui/main_hover.png'
            if not self.base_button_image_size:
                self.base_button_image_size = renpy.image_size(idle_image) #(174, 38)
            image_size = self.base_button_image_size
            button_sizes = {
             'xmaximum': int((kwargs.get('xmaximum', 0) or image_size[0] * scale) - kwargs.get('right_margin', 0)),
             'ymaximum': kwargs.get('ymaximum', 0) or int(image_size[1] * scale),
            }
            kwargs.setdefault('xmaximum', int(image_size[0] * scale))
            kwargs.setdefault('ymaximum', int(image_size[1] * scale))
            def scaler(image, scale, kwargs):
                return im.Scale(image, kwargs['xmaximum'], kwargs['ymaximum'])
            ui.imagebutton(
                idle_image=Fixed(
                    scaler(Image(idle_image), scale, button_sizes),
                    Text(text, xalign=.5, yalign=.5),  #, outlines=[(1, '#808080', 0, 0)]),),
                ),
                hover_image=Fixed(
                    scaler(Image(hover_image), scale, button_sizes),
                    Text(text, xalign=.5, yalign=.5),  #, outlines=[(1, '#808080', 0, 0)]),),
                ),
                selected_idle=Fixed(
                    scaler(Image(idle_image), scale, button_sizes),
                    Text(text, xalign=.5, yalign=.5),  #, outlines=[(1, '#808080', 0, 0)]),),
                ),
                selected_hover=Fixed(
                    scaler(Image(hover_image), scale, button_sizes),
                    Text(text, xalign=.5, yalign=.5),  #, outlines=[(1, '#808080', 0, 0)]),),
                ),
                action=action, #SetVariable('image_button_test', True),
                focus_mask=True,
                xpos=xpos,
                ypos=ypos,
                **kwargs
            )

        def main_button(self, text='Gallery', action=None, xpos=None, ypos=None, reverse=False):
            if action is None:
                # supply a default action; so we can manage transitions and all that at a later date
                # without mucking with the main menu
                action = [GalleryManager.ShowMenu(), Show("gallery_grid", transition=dissolve)]
            #remove alpha pixels to base-line with existing buttons
            return self.base_button(text, action, xpos=xpos-4, ypos=ypos-4, reverse=reverse)

        def button(self, text, action=None, **kwargs):
            kwargs.setdefault('right_margin', 6)
            kwargs.setdefault('scale', .8)
            return self.base_button(text, action, **kwargs)

        # cache implementation (ideally this would be defined elsewhere and only referenced in here)

        def lru_cache(maxsize=100, typed=False):
            """ Least-recently-used cache decorator. (see: python 3.2 implementation)
            """

            from collections import namedtuple
            from functools import update_wrapper
            from threading import RLock

            _CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currsize"])

            class _HashedSeq(list):
                __slots__ = 'hashvalue'

                def __init__(self, tup, hash=hash):
                    self[:] = tup
                    self.hashvalue = hash(tup)

                def __hash__(self):
                    return self.hashvalue

            def decorating_function(user_function):
                cache = dict()
                stats = [0, 0]                  # make statistics updateable non-locally
                HITS, MISSES = 0, 1             # names for the stats fields
                #make_key = _make_key
                cache_get = cache.get           # bound method to lookup key or return None
                _len = len                      # localize the global len() function
                lock = RLock()                  # because linkedlist updates aren't threadsafe
                root = []                       # root of the circular doubly linked list
                root[:] = [root, root, None, None]      # initialize by pointing to self
                nonlocal_root = [root]                  # make updateable non-locally
                PREV, NEXT, KEY, RESULT = 0, 1, 2, 3    # names for the link fields

                def make_key(args, kwds, typed,
                     kwd_mark = (object(),),
                     fasttypes = {int, str, frozenset, type(None)},
                     sorted=sorted, tuple=tuple, type=type, len=len):
                        'Make a cache key from optionally typed positional and keyword arguments'
                        key = args
                        if kwds:
                            sorted_items = sorted(kwds.items())
                            key += kwd_mark
                            for item in sorted_items:
                                key += item
                        if typed:
                            key += tuple(type(v) for v in args)
                            if kwds:
                                key += tuple(type(v) for k, v in sorted_items)
                        elif len(key) == 1 and type(key[0]) in fasttypes:
                            return key[0]
                        return _HashedSeq(key)

                if maxsize == 0:
                    def wrapper(*args, **kwds):
                        # no caching, just do a statistics update after a successful call
                        result = user_function(*args, **kwds)
                        stats[MISSES] += 1
                        return result

                elif maxsize is None:
                    def wrapper(*args, **kwds):
                        # simple caching without ordering or size limit
                        key = make_key(args, kwds, typed)
                        result = cache_get(key, root)   # root used here as a unique not-found sentinel
                        if result is not root:
                            stats[HITS] += 1
                            return result
                        result = user_function(*args, **kwds)
                        cache[key] = result
                        stats[MISSES] += 1
                        return result

                else:
                    def wrapper(*args, **kwds):
                        # size limited caching that tracks accesses by recency
                        key = make_key(args, kwds, typed) if kwds or typed else args
                        with lock:
                            link = cache_get(key)
                            if link is not None:
                                # record recent use of the key by moving it to the front of the list
                                root, = nonlocal_root
                                link_prev, link_next, key, result = link
                                link_prev[NEXT] = link_next
                                link_next[PREV] = link_prev
                                last = root[PREV]
                                last[NEXT] = root[PREV] = link
                                link[PREV] = last
                                link[NEXT] = root
                                stats[HITS] += 1
                                return result
                        result = user_function(*args, **kwds)
                        with lock:
                            root, = nonlocal_root
                            if key in cache:
                                # same key was added to the cache while the lock was released.
                                pass
                            elif _len(cache) >= maxsize:
                                # use the old root to store the new key and result
                                oldroot = root
                                oldroot[KEY] = key
                                oldroot[RESULT] = result
                                # empty the oldest link and make it the new root
                                root = nonlocal_root[0] = oldroot[NEXT]
                                oldkey = root[KEY]
                                oldvalue = root[RESULT]
                                root[KEY] = root[RESULT] = None
                                # now update the cache dictionary for the new links
                                del cache[oldkey]
                                cache[key] = oldroot
                            else:
                                # put result in a new link at the front of the list
                                last = root[PREV]
                                link = [last, root, key, result]
                                last[NEXT] = root[PREV] = cache[key] = link
                            stats[MISSES] += 1
                        return result

                def cache_info():
                    """Report cache statistics"""
                    with lock:
                        return _CacheInfo(stats[HITS], stats[MISSES], maxsize, len(cache))

                def cache_clear():
                    """Clear the cache and cache statistics"""
                    with lock:
                        cache.clear()
                        root = nonlocal_root[0]
                        root[:] = [root, root, None, None]
                        stats[:] = [0, 0]

                wrapper.__wrapped__ = user_function
                wrapper.cache_info = cache_info
                wrapper.cache_clear = cache_clear
                return update_wrapper(wrapper, user_function)

            return decorating_function

        @lru_cache()    #this function is so fast, we don't really need this
        # but we can reduce file access this way (assuming the os didn't do that for us already)
        def get_image_size(self, file_path):
            """
            gets an image's size, because asking renpy to do it is expensive
            supported formats: jpeg, gif, & png
            returns (width, height) for a given img file content
            raises on read failures & unknown formats
            """

            import os, struct

            class UnknownImageFormat(Exception):
                pass

            with renpy.file(file_path) as input:
                height = -1
                width = -1
                data = input.read(25)
                msg = " raised while trying to decode as JPEG."

                if data[:6] in ('GIF87a', 'GIF89a'):
                    # GIFs
                    w, h = struct.unpack("<HH", data[6:10])
                    width = int(w)
                    height = int(h)
                elif data.startswith('\211PNG\r\n\032\n') and (data[12:16] == 'IHDR'):
                    # PNGs
                    w, h = struct.unpack(">LL", data[16:24])
                    width = int(w)
                    height = int(h)
                elif data.startswith('\211PNG\r\n\032\n'):
                    # older PNGs
                    w, h = struct.unpack(">LL", data[8:16])
                    width = int(w)
                    height = int(h)
                elif data.startswith('\377\330'):
                    # JPEG
                    input.seek(0)
                    input.read(2)
                    b = input.read(1)
                    try:
                        while (b and ord(b) != 0xDA):
                            while (ord(b) != 0xFF): b = input.read(1)
                            while (ord(b) == 0xFF): b = input.read(1)
                            if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                                input.read(3)
                                h, w = struct.unpack(">HH", input.read(4))
                                break
                            else:
                                input.read(int(struct.unpack(">H", input.read(2))[0])-2)
                            b = input.read(1)
                        width = int(w)
                        height = int(h)
                    except struct.error:
                        raise UnknownImageFormat("StructError" + msg)
                    except ValueError:
                        raise UnknownImageFormat("ValueError" + msg)
                    except Exception as e:
                        raise UnknownImageFormat(e.__class__.__name__ + msg)
                else:
                    raise UnknownImageFormat("Sorry, don't know how to get the size of this file.")

            return width, height

        # the gallery

        def __init__(self):
            self._unlock_all = False
            #there should be no filtering at first; some things, such as buttons, are built only on init
            self._filter = 'all'
            self._subfilter = 'all'
            self.gallery = None
            self.items = []
            self.unlocked = []   #images to unlock regardless whether they've been seen or not
            self.next_action = None
            self.gallery_buttons = []
            #config.image_cache_size = 8    #8 is default
            #im.cache.init()
            self._sort_reverse = False
            self.locations = set()
            self.filters = ['all', 'location', 'locked', 'unlocked']

            #image size "cache" (it's apparently an expensive operation)
            self.base_button_image_size = False

            #rows and columns in the gallery screens
            self.rows = 4
            self.cols = 3

            #(267x150) will work well with 16:9 screen ratio.
            #thumbnail size in pixels:
            self.thumbnail_x = 267
            self.thumbnail_y = 150

            self.page = 0
            self.next_page = 0
            self.cells = self.rows * self.cols

            self.get_gallery_items()
            self.build_gallery()
            self.build_thumbnails()
            self.build_buttons()

        def get_gallery_items(self):
            #find loaded images, and put them in the gallery (undocumented version):
            #this requires us to be last; everyone should have imported what they want by now
            from renpy.display import image as rp_img
            for img_name, img_obj in rp_img.images.iteritems():
                try:
                    if 'gui' in img_obj.filename or 'cache' in img_obj.filename: #ignore these
                        continue
                    self.items.append(' '.join(img_name))
                except AttributeError:
                    pass    #we don't care about images with no names

            self.all_items = self.items #for filters; so we don't have to run this over and over again

        def build_gallery(self):
            self.gallery = Gallery()
            #this doesn't seem to work: renpy.get_physical_size()
            win_size = (config.screen_width, config.screen_height)
            from renpy.display import image as rp_img
            import re
            location_regex = r'''locations/(.*?)/'''
            self.locations = set(['all'])

            for gallery_item in self.all_items:
                self.gallery.button(gallery_item + " button")
                self.gallery.image(gallery_item)
                try:    #scroll if too big
                    fname = rp_img.images[tuple(gallery_item.split(' '))].filename
                    img_size = self.get_image_size(fname)
                    if img_size[0] > win_size[0] and img_size[1] > win_size[1]:
                        #both width and height constrained
                        self.gallery.transform(gallery_instant_zoom)
                        pass
                    elif img_size[0] > win_size[0]:
                        #width constrained
                        self.gallery.transform(gallery_scroll_x)
                    elif img_size[1] > win_size[1]:
                        #height constrained
                        self.gallery.transform(gallery_scroll_y)
                except:
                    pass
                if gallery_item not in self.unlocked and not self._unlock_all:
                    self.gallery.unlock(gallery_item)

                #build a list of locations
                try:
                    location = re.search(location_regex, fname).groups()[0]
                    self.locations.add(location)
                except:
                    pass

            self.gallery.transition = fade
            self.filter_gallery()

        def sort_gallery(self):
            from renpy.display import image as rp_img
            #sort by filename
            self.items = sorted(self.items, key=lambda x: rp_img.images[tuple(x.split(' '))].filename, reverse=self.sort_reverse)

        def filter_gallery(self):
            from renpy.display import image as rp_img
            if self.filter == 'all':
                self.items = self.all_items
            elif self.filter == 'location':
                self.items = []
                for i in self.all_items:
                    filename = rp_img.images[tuple(i.split(' '))].filename
                    if 'locations' in filename:
                        if self.subfilter == 'all' or self.subfilter in filename:
                            self.items.append(i)
            elif self.filter == 'locked':
                self.items = [name for name in self.all_items if not renpy.seen_image(name)]
            elif self.filter == 'unlocked':
                self.items = [name for name in self.all_items if renpy.seen_image(name)]
            #if we want characters, we'll probably have to parse chars.rpy for their definitions

            if self.page > self.pages:
                self.page = 0

            self.sort_gallery()

        def build_thumbnails(self):
            #Avast, here there be thumbnails!
            from renpy.display import image as rp_img
            for gallery_item in self.all_items:
                try:    #factor scale
                    fname = rp_img.images[tuple(gallery_item.split(' '))].filename
                    img = renpy.image(gallery_item + " button",
                        im.FactorScale(ImageReference(gallery_item),
                            min(float(self.thumbnail_x) / self.get_image_size(fname)[0],
                            float(self.thumbnail_y) / self.get_image_size(fname)[1])
                        ),
                    )
                except: #factor scale failed, fallback to regular scaling
                    renpy.image(gallery_item + " button", im.Scale(ImageReference(gallery_item), self.thumbnail_x, self.thumbnail_y))
                img = renpy.image(gallery_item + " button disabled", im.Grayscale(ImageReference(gallery_item + " button")))

        def preload_images(self):
            from renpy.display import image as rp_img

            #items of interest
            preloadables = []

            #load current page
            start = gallery.page * gallery.cells
            end = min((gallery.page + 1) * gallery.cells, len(gallery.items))
            preloadables += [self.items[i] for i in range(start, end)]
            '''
            #load the first page
            start = 0
            end = min(gallery.cells, len(gallery.items))
            preloadables += [self.items[i] for i in range(start, end)]

            #load last page
            start = gallery.pages * gallery.cells
            end = len(gallery.items)
            preloadables += [self.items[i] for i in range(start, end)]

            #load previous page
            prev_page = gallery.page - 1
            if prev_page > 0:
                start = prev_page * gallery.cells
                end = min((prev_page + 1) * gallery.cells, len(gallery.items))
                preloadables += [self.items[i] for i in range(start, end)]
            '''
            for gallery_item in preloadables:
                try:    #we try to help; we're at the mercy of the renderer after this
                    #load only what we need
                    if renpy.seen_image(gallery_item) or self.unlock_all:
                        img = rp_img.images[tuple((gallery_item + " button").split(' '))]
                        #im.cache.preload_image(img)
                        im.cache.get(img)
                    else:
                        img = rp_img.images[tuple((gallery_item + " button disabled").split(' '))]
                        #im.cache.preload_image(img)
                        im.cache.get(img)
                except:
                    pass

        def build_buttons(self):
            #make the buttons
            self.gallery_buttons = {}
            for gallery_item in self.all_items:
                self.gallery_buttons[gallery_item] = self.make_button(gallery_item + " button",
                        gallery_item + " button",
                        gallery_item + " button disabled",
                        xalign=0.5, yalign=0.5,
                        idle_border=None, background=None, bottom_margin=24,
                )

        @property
        def items_total(self):
            return len(self.items)

        @property
        def unlocked_total(self):
            return sum([renpy.seen_image(name) for name in self.items])

        @property
        def pages(self):
            return int(math.floor(self.items_total / float(self.cells))) - (1 if not self.items_total % self.cells else 0)

        @property
        def sort_reverse(self):
            return self._sort_reverse

        @sort_reverse.setter
        def sort_reverse(self, val):
            self._sort_reverse = val
            self.sort_gallery()

        @property
        def filter(self):
            return self._filter

        @filter.setter
        def filter(self, val):
            self.page = 0
            self._filter = val
            #reset subfilter; all filters should support the 'all' subfilter
            self._subfilter = 'all'
            self.filter_gallery()

        @property
        def subfilter(self):
            return self._subfilter

        @subfilter.setter
        def subfilter(self, val):
            self.page = 0
            self._subfilter = val
            self.filter_gallery()

        @property
        def unlock_all(self):
            return self._unlock_all

        @unlock_all.setter
        def unlock_all(self, val):
            self._unlock_all = val
            self.build_gallery()
            self.build_buttons()

        def make_button(self, *args, **kwargs):
            ''' make_button wrapper '''
            button = self.gallery.make_button(*args, **kwargs)
            return button

        def get_action(self):
            return self.next_action or NullAction()

        # button actions

        #NOTE: Originally, there were custom actions instead of functions,
        # but the execution and maintenance overhead was considered too much.
        # The goal was to simplify the gallery screen's layout, offloading the action lists grunt work elsewhere.
        # An additional benefit was full control over actions through python,
        # but that can be emulated with less overhead through custom field setters.
        # Function calls add some overhead too (compared to inline actions lists), but not nearly as much,
        # and still accomplish the original goal.
        # Originally, there was an empty gallery instead of an empty grid, which duplicated most of the gallery's layout.
        # Extracting the grid made transitions a little more complex,
        # but greatly simplified maintaining the original gallery screen's layout.

        def pre_transition(self):
            return [Hide('gallery_grid', transition=dissolve)]

        def post_transition(self):
            return [Show('gallery_empty_grid')]

        def next(self):
            return self.pre_transition() + [
                SetField(gallery, 'next_action',
                    SetField(gallery, 'page', gallery.next_page if gallery.next_page <= gallery.pages else 0)),
            ] + self.post_transition()  #GalleryManager.ShowMenu("empty_gallery")]

        def back(self):
            return self.pre_transition() + [
                SetField(gallery, 'next_action',
                    SetField(gallery, 'page', gallery.page - 1 if gallery.page != 0 else gallery.pages)),
            ] + self.post_transition()  #GalleryManager.ShowMenu("empty_gallery")]

        def first(self):
            return self.pre_transition() + [
                SetField(gallery, 'next_action', SetField(gallery, 'page', 0)),
            ] + self.post_transition()  # GalleryManager.ShowMenu("empty_gallery")]

        def last(self):
            return self.pre_transition() + [
                SetField(gallery, 'next_action', SetField(gallery, 'page', gallery.pages)),
            ] + self.post_transition()  # GalleryManager.ShowMenu("empty_gallery")]

        def close(self):    #because return is a keyword
            return [
                Hide('gallery_filter_menu'),
                Hide('gallery_location_menu'),
                Hide('gallery_grid'),
                GalleryManager.ShowMenu("main_menu"),
            ]

        def apply_filter(self, filter):
            return self.pre_transition() + [
                Hide('gallery_filter_menu'), Hide('gallery_location_menu'),
                SetField(self, 'next_action', SetField(self, 'filter', filter)),
            ] + self.post_transition()  # GalleryManager.ShowMenu("empty_gallery")]

        def apply_subfilter(self, location):
            return self.pre_transition() + [
                Hide('gallery_filter_menu'), Hide('gallery_location_menu'),
                SetField(self, 'next_action', SetField(self, 'subfilter', location)),
            ] + self.post_transition()  # GalleryManager.ShowMenu("empty_gallery")]

        def unlock(self):
            return self.pre_transition() + [
                SetField(self, 'next_action', ToggleField(self, 'unlock_all')),
            ] + self.post_transition()  # GalleryManager.ShowMenu("empty_gallery")]

        def cancel_menu(self):
            return [Hide('gallery_filter_menu'), Hide('gallery_location_menu')]

        def resort(self):
            return self.pre_transition() + [
                SetField(self, 'next_action', ToggleField(self, 'sort_reverse')),
            ] + self.post_transition()  # GalleryManager.ShowMenu("empty_gallery")]

        def show_filter_menu(self):
            return [Hide('gallery_location_menu'), ShowMenu('gallery_filter_menu')]

        def show_subfilter_menu(self):
            return [Hide('gallery_filter_menu'), ShowMenu('gallery_location_menu')]

init 9001 python:

    gallery = GalleryManager()

image gallery_background = im.Sepia(Image('images/ui/mm_ground.png'))


screen gallery_filter_menu:
    frame yalign 0.5 xalign 0.5:
        vbox:
            for filter in gallery.filters:
                textbutton  filter.replace('_', ' ').title() xminimum 256 xalign 0.5 yalign 0.5 action gallery.apply_filter(filter)
            textbutton 'Cancel' xminimum 256 xalign 0.5 yalign 0.5 action gallery.cancel_menu()

screen gallery_location_menu:
    frame yalign 0.5 xalign 0.5:
        vbox:
            for location in gallery.locations:
                textbutton  location.replace('_', ' ').title() xminimum 256 xalign 0.5 yalign 0.5 action gallery.apply_subfilter(location)
            textbutton 'Cancel' xminimum 256 xalign 0.5 yalign 0.5 action gallery.cancel_menu()

screen gallery_empty_grid:
    frame xalign 0.5 yalign 0.5:
        style_group 'gallery_menu_style'
        style 'gallery_menu_style'
        #wait long enough for transition, then do what we need to do
        timer 0.5 action gallery.get_action()
        #transition back to the gallery
        timer 0.6 action [Hide('gallery_empty_grid'), GalleryManager.ShowMenu("gallery_grid")]

screen gallery_grid:
    frame xalign 0.5 yalign 0.5:
        style_group 'gallery_menu_style'
        style 'gallery_menu_style'
        grid gallery.rows gallery.cols:
            style_group 'gallery_menu_style'
            style 'gallery_menu_style'
            xalign 0.5
            yalign 0.5
            $ i = 0
            $ gallery.next_page = gallery.page + 1
            if gallery.next_page > gallery.pages:
                $ gallery.next_page = 0
            $ gallery_start = gallery.page * gallery.cells
            $ gallery_end = min((gallery.page + 1) * gallery.cells, len(gallery.items))
            for i in range(gallery_start, gallery_end):
                    add gallery.gallery_buttons[gallery.items[i]]
            for j in range(gallery_end, (gallery.page + 1) * gallery.cells):
                null

screen gallery:
    tag menu
    use navigation
    frame background 'gallery_background' xalign 0.5 yalign 0.5:
        #ensure the gallery grid is shown (if someone shows the gallery without showing the grid)
        timer 0.5 action Show("gallery_grid", transition=dissolve)

        vbox:
            style_group 'gallery_menu_style'
            yalign 0.97
            style 'gallery_menu_style'

            frame:
                style_group 'gallery_menu_style'
                style 'gallery_menu_style'
                hbox:
                    text "Filter: " style 'gallery_stats_text_style' yalign 0.5
                    $ gallery.button(_(gallery.filter.title()), action=gallery.show_filter_menu())
                    if gallery.filter == 'location':
                     $ gallery.button(_(gallery.subfilter.replace('_', ' ').title()), action=gallery.show_subfilter_menu(), xmaximum=245)
                    text "Sort: " style 'gallery_stats_text_style' yalign 0.5
                    $ gallery.button(_("Default") if not gallery.sort_reverse else _("Reverse"), action=gallery.resort())

            frame:
                style_group 'gallery_menu_style'
                style 'gallery_menu_style'
                hbox:
                    $ gallery.button(_("First"), gallery.first())
                    $ gallery.button(_("Back"), gallery.back())
                    $ gallery.button(_("Next"), gallery.next())
                    $ gallery.button(_("Last"), gallery.last())
                    $ gallery.button(_("Return"), gallery.close())

                    $ page_text = " Page: %s / %s " % (gallery.page + 1, gallery.pages + 1)
                    $ completed_text = " Completion: [gallery.unlocked_total] / [gallery.items_total] "
                    text page_text style 'gallery_stats_text_style' yalign 0.5
                    text completed_text style 'gallery_stats_text_style' yalign 0.5

# NOTE: Disable "simple" unlock.
#        frame:
#            style_group 'gallery_menu_style'
#            yalign 0.97
#            xalign 1.0
#            style 'gallery_menu_style'
#            hbox:
#                $ gallery.button(_("Lock") if gallery.unlock_all else _("Unlock"), xalign=1.0, action=gallery.unlock())
