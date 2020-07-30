"""
- Show surface description when the user's mouse hovers over the surface
number in the cell block. Ignore commented surfaces. if the surface was
not found, a warning message pops up.
- Show material description ('$' comment on the first line of material card)
"""

import sublime
import sublime_plugin
import re


class ShowSurfaceDescription(sublime_plugin.ViewEventListener):
    @classmethod
    def is_applicable(cls, settings):
        syntax = settings.get('syntax')
        if syntax == 'Packages/User/mcnp.sublime-syntax':
            return True

    @classmethod
    def applies_to_primary_view_only(cls):
        ''' Apply on_hover to all views of file '''
        return False

    def on_hover(self, point: int, hover_zone: int):
        v = self.view
        # show surface description
        cur_pos_row = v.rowcol(point)[0]
        cur_line = sublime.Region(v.text_point(cur_pos_row, 0),
                                  v.text_point(cur_pos_row, 80))
        cell_start = v.rowcol(v.find('Begin Cells', 0).b)[0]
        surf_start = v.rowcol(v.find('Begin Surfaces', 0).b)[0]
        mat_start = v.rowcol(v.find('Begin Materials', 0).b)[0]
        tal_start = v.rowcol(v.find('Begin Tallies', 0).b)[0]
        rcm_start = v.rowcol(v.find('REACTOR CORE MAP', 0).b)[0]
        rcm_region = range(rcm_start + 1, rcm_start + 18)
        match_surf = v.match_selector(point, "-(comment.line, \
                                               storage.type.class.python, \
                                               entity.name.python, \
                                               keyword.import, \
                                               string.quoted.single.ruby, \
                                               source.python, \
                                               meta.function.parameters. \
                                               default-value.python, \
                                               constant.language.python, \
                                               variable.language.python, \
                                               source.yaml \
                                               string.unquoted.plain.out.yaml \
                                               entity.name.tag.yaml)")
        surf_number = v.substr(v.word(point))
        if (match_surf and cell_start <= cur_pos_row <= surf_start
               and cur_pos_row not in rcm_region
               and surf_number.strip() != ""):
            if (hover_zone != sublime.HOVER_TEXT or v.is_popup_visible()):
                return
            surf_block = sublime.Region(v.text_point(surf_start + 1, 0),
                                        v.text_point(mat_start + 1, 0))
            lines = v.lines(surf_block)
            surf = ""
            for i, line in enumerate(lines):
                find_surf = v.find('^' + surf_number + ' ', line.a)
                if find_surf and find_surf.a == line.a:
                    line_number_s = i + surf_start + 2
                    surf_num = v.substr(line)[:5].rstrip()
                    surf = v.substr(line)[5:].lstrip()
                    surf_tr = re.search(r'^\d*', surf).group()
                    surf_type = re.search(r'\b(?i)[a-z]/?[a-z]*1?',
                                          surf).group()
                    comment_match = re.search(r'\$.*', surf)
                    if comment_match:
                        comment = comment_match.group()
                    else:
                        comment = ""
                    surf_entr = re.sub(r'\s', '&nbsp;',
                                       surf.lstrip(surf_tr).lstrip().lstrip(
                                           surf_type).rstrip(comment))
                    sp_r = '<span style="color: #FF6347;">'
                    sp_o = '<span style="color: #FFA500;">'
                    sp_g = '<span style="color: #98FB98;">'
                    sp_y = '<span style="color: #F0E68C;">'
                    sp_wh = '<span style="color: DCDCDC; white-space: pre;">'
                    sp_end = '</span>'
                    surf = (sp_o + '<a href="show_surf">' + surf_num
                            + '</a>&nbsp;' + sp_end + sp_y
                            + surf_tr + '&nbsp;&nbsp;' + sp_end + sp_r
                            + surf_type + sp_end + sp_wh + surf_entr + sp_end
                            + sp_g + '&nbsp;&nbsp;' + comment + sp_end)
                    break
                else:
                    surf = '<span style="color:red; \
                            background-color: #FFFF00">\
                           <b> &nbsp;Surface was not found. </b> </span>'
            content = ('<body>' + surf + '</body>')

            def navigate(href):
                if href == 'show_surf':
                    cell_numb = v.substr(v.find('^\d+',
                                                v.text_point(v.rowcol(point)[0]
                                                             + 0, 0)))
                    p = v.text_point(line_number_s - 1, 0)
                    ph_content = '<body id="whitespace"><span class="w"> \
                        <a href="cb"> ↑ ' + cell_numb + '</a></span></body>'

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
                    v.sel().add(v.text_point(line_number_s - 1, 0))
                    v.show(v.sel())

            v.show_popup(content, sublime.HIDE_ON_MOUSE_MOVE_AWAY, point,
                         1000, 800, on_navigate=navigate)
            lines.clear()

        # show material description
        selector = "source.yaml string.unquoted.plain.out.yaml\
                    entity.name.tag.yaml"
        match_mat_hover = v.match_selector(point, selector)
        match_mat_re = re.search(r'^\d+', v.substr(cur_line)[5:].lstrip())
        mat_number = v.substr(v.word(point))
        if (match_mat_hover and cell_start <= cur_pos_row <= surf_start
                and mat_number == match_mat_re.group()):
            if (hover_zone != sublime.HOVER_TEXT or v.is_popup_visible()):
                return
            mat_block = sublime.Region(v.text_point(mat_start + 1, 0),
                                       v.text_point(tal_start + 1, 0))
            lines = v.lines(mat_block)
            for i, line in enumerate(lines):
                if mat_number == "0":
                    mat_comment = '<span style="color: #98FB98;"> void cell \
                                   </span>'
                    break
                find_mat = v.find(r'^m' + mat_number + '(?=\s)', line.a)
                if find_mat and find_mat.a == line.a:
                    line_number_m = i + mat_start + 2
                    mat_comment_mantch = re.search(r'\$.*', v.substr(line))
                    if mat_comment_mantch:
                        mat_comment = ('<span style="color: \
                                        #FFA500;"><a href="show_mat">'
                                       + mat_number + '</a>&nbsp;&nbsp;</span>\
                                       <span style="color: #98FB98;">'
                                       + mat_comment_mantch.group().lstrip('$')
                                       + '</span>')
                    else:
                        mat_comment = "no comment"
                    break
                else:
                    mat_comment = '<span style="color:red; \
                                    background-color: #FFFF00"> <b> &nbsp; \
                                    Material was not found. </b> </span>'
            content = ('<body>' + mat_comment + '</body>')

            def navigate(href):
                if href == 'show_mat':
                    cell_numb = v.substr(v.find('^\d+',
                                                v.text_point(v.rowcol(point)[0]
                                                             + 0, 0)))
                    p = v.text_point(line_number_m - 1, 0)
                    ph_content = '<body id="whitespace"><span class="w"> \
                        <a href="cb"> ↑ ' + cell_numb + '</a></span></body>'

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
                    v.sel().add(p)
                    v.show(v.sel())
            v.show_popup(content, sublime.HIDE_ON_MOUSE_MOVE_AWAY, point,
                         1000, 800, on_navigate=navigate)
            lines.clear()
