"""
 Show universe description in active core map.
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
      core_map = v.find(r'^\s{5}\s*(0\s\s?){6}(\d\s+){17}', 0)
      if core_map:
          print("Core map was found.")
      else:
          print("Core map wasn't found")


    def on_hover(self, point: int, hover_zone: int):
        v = self.view
        # show surface description
        cell_start = v.rowcol(v.find('Begin Cells', 0).b)[0]
        surf_start = v.rowcol(v.find('Begin Surfaces', 0).b)[0]
        rcm_start = v.rowcol(v.find('REACTOR CORE MAP', 0).b)[0]
        rcm_region = sublime.Region(v.text_point(rcm_start + 1, 0),
                                    v.text_point(rcm_start + 18, 0))
        match_element = v.match_selector(point, "-(comment.line)")
        element_number = v.substr(v.word(point))
        if (match_element and rcm_region.contains(point)
               and element_number.strip() != ""):
            if (hover_zone != sublime.HOVER_TEXT or v.is_popup_visible()):
                return
            line_number = rcm_start + 17 - v.rowcol(point)[0]
            line = v.substr(sublime.Region(v.text_point(v.rowcol(point)[0], 0),
                                           point))
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

            cells_block = sublime.Region(v.text_point(cell_start + 1, 0),
                                                  v.text_point(surf_start + 1, 0))
            universe = v.find('u=' + element_number + '(\n|\s)', cells_block.a)
            if universe and not re.match(r'^c', v.substr(v.line(universe))):
                u_title = v.substr(v.line(v.text_point(v.rowcol(universe.a)[0] - 2, 0)))[2:].strip()
                sp_g = '<span style="color: #98FB98;">'
                sp_end = '</span>'
                map_cell_descr = (sp_g + 'Universe:&nbsp;&nbsp; \
                                  &nbsp;&nbsp;'
                                  + sp_end + element_number  + '<br>'
                                  + sp_g + 'Ячейка а.з.&nbsp;&nbsp;&nbsp;'
                                  + sp_end + str(line_number) + '-'
                                  + str(column) + '<br>' + sp_g
                                  + 'Элемент а.з.&nbsp;&nbsp;' + sp_end
                                  + '<a href="show_u">' + u_title + '</a>')

            else:
                if element_number == '0':
                    map_cell_descr = '<span style="color: #98FB98;"> \
                                      Empty cell.</span>'
                else:
                    map_cell_descr = "<span style='color:red; \
                                     background-color: #FFFF00'>\
                                     <b> &nbsp;Universe wasn't found. \
                                     Maybe it commented out. </b> </span>"
            content = ('<body>' + map_cell_descr + '</body>')
            #         sp_wh = '<span style="color: DCDCDC; white-space: pre;">'
            #         sp_end = '</span>'

            def navigate(href):
                if href == 'show_u':
                    p = v.text_point(v.rowcol(universe.a)[0] - 2, 0)
                    ph_content = '<body id="whitespace"><span class="w"> \
                        <a href="cb"> ↑ to reactor core map</a></span></body>'

                    def come_back(href):
                        if href == 'cb':
                            v.erase_phantoms("come_back")
                            v.sel().clear()
                            v.sel().add(point)
                            v.show(v.sel())

                    v.add_phantom("come_back", sublime.Region(p, p),
                                  ph_content, sublime.LAYOUT_INLINE,
                                  on_navigate=come_back)
                    v.sel().clear()
                    v.sel().add(v.text_point(v.rowcol(universe.a)[0] - 2, 0))
                    v.show(v.sel())

            v.show_popup(content, sublime.HIDE_ON_MOUSE_MOVE_AWAY, point,
                         1000, 800, on_navigate=navigate)
