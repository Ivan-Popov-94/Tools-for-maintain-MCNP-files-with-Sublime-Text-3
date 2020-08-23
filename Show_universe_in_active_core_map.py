"""
 Show popup with universe description in active core map.
 Description includes:
 - universe number
 - reactor core cell in form row-column
 - title of cells with this universe from cell block
"""

import sublime
import sublime_plugin
import re


class ShowUniverseDescription(sublime_plugin.ViewEventListener):
    @classmethod
    def is_applicable(cls, settings):
        syntax = settings.get('syntax')
        if syntax == 'Packages/User/mcnp.sublime-syntax':
            return True

    @classmethod
    def applies_to_primary_view_only(cls):
        ''' Apply on_hover to all views of file '''
        return False

    def on_load(self):
        v = self.view.window().active_view()
        # find first line of reactor core map
        core_map = v.find(r'^\s{5}\s*(0\s\s?){6}(\d\s+){17}', 0)
        if core_map:
            print("Core map was found.")
        else:
            print("Core map wasn't found")

    def on_hover(self, point: int, hover_zone: int):
        v = self.view
        cell_start = v.rowcol(v.find('Begin Cells', 0).b)[0]
        surf_start = v.rowcol(v.find('Begin Surfaces', 0).b)[0]
        # find title of reactor core map and create region with it
        rcm_start = v.rowcol(v.find('REACTOR CORE MAP', 0).b)[0]
        rcm_region = sublime.Region(v.text_point(rcm_start + 1, 0),
                                    v.text_point(rcm_start + 18, 0))
        # ignore comments on hover event
        match_element = v.match_selector(point, "-(comment.line)")
        # take number under cursor
        element_number = v.substr(v.word(point))
        # if cursor inside reactor core map and on a number
        if (match_element and rcm_region.contains(point)
                and element_number.strip() != ""):
            if (hover_zone != sublime.HOVER_TEXT or v.is_popup_visible()):
                return
            # get line number (row of cells in reactor core map)
            # reverse order in input deck!
            line_number = rcm_start + 17 - v.rowcol(point)[0]
            # content of line
            line = v.substr(sublime.Region(v.text_point(v.rowcol(point)[0], 0),
                                           point))
            # get column number
            # considering that zeros in the first 6 lines are not counted
            column = len(re.findall(r'\d+', line[:-2])) + 1
            if line_number == 13:
                column -= 6
            elif line_number == 12:
                column -= 5
            elif line_number == 11:
                column -= 4
            elif line_number == 10:
                column -= 3
            elif line_number == 9:
                column -= 2
            elif line_number == 8:
                column -= 1

            # get cell block in input deck
            cells_block = sublime.Region(v.text_point(cell_start + 1, 0),
                                         v.text_point(surf_start + 1, 0))
            # find first occurrence of universe in cell_block (not commented)
            universe = v.find('u=' + element_number + '(\n|\s)', cells_block.a)
            if universe and not re.match(r'^c', v.substr(v.line(universe))):
                # get title of cells with such universe
                u_title = v.substr(v.line(v.text_point(v.rowcol(universe.a)[0]
                                                       - 2, 0)))[2:].strip()

                # compose description of universe for popup
                sp_g = '<span style="color: #98FB98;">'
                sp_end = '</span>'
                map_cell_descr = (sp_g + 'Universe:&nbsp;&nbsp; \
                                  &nbsp;&nbsp;'
                                  + sp_end + element_number + '<br>'
                                  + sp_g + 'Ячейка а.з.&nbsp;&nbsp;&nbsp;'
                                  + sp_end + str(line_number) + '-'
                                  + str(column) + '<br>' + sp_g
                                  + 'Элемент а.з.&nbsp;&nbsp;' + sp_end
                                  + '<a href="show_u">' + u_title + '</a>')
            # if universe wasn't found in cell block
            else:
                # Check for zero
                if element_number == '0':
                    map_cell_descr = '<span style="color: #98FB98;"> \
                                      Empty cell.</span>'
                # Warning message for other options
                else:
                    map_cell_descr = "<span style='color:red; \
                                     background-color: #FFFF00'>\
                                     <b> &nbsp;Universe wasn't found. \
                                     Maybe it commented out. </b> </span>"
            content = ('<body>' + map_cell_descr + '</body>')

            def navigate(href):
                '''  Go to title of universe and come back via hyperlink '''
                if href == 'show_u':
                    # text poin in begin of line with universe title
                    p = v.text_point(v.rowcol(universe.a)[0] - 2, 0)
                    # phantom content for come back popup
                    ph_content = '<body id="whitespace"><span class="w"> \
                        <a href="cb"> ↑ to reactor core map</a></span></body>'

                    def come_back(href):
                        ''' return to reactor core map '''
                        if href == 'cb':
                            v.erase_phantoms("come_back")
                            v.sel().clear()
                            v.sel().add(point)
                            v.show(v.sel())

                    v.add_phantom("come_back", sublime.Region(p, p),
                                  ph_content, sublime.LAYOUT_INLINE,
                                  on_navigate=come_back)
                    v.sel().clear()
                    # go to universe title
                    v.sel().add(v.text_point(v.rowcol(universe.a)[0] - 2, 0))
                    v.show(v.sel())

            v.show_popup(content, sublime.HIDE_ON_MOUSE_MOVE_AWAY, point,
                         1000, 800, on_navigate=navigate)
