"""
This plugin helps you to avoid dublicates of cell/surface/material/tally
number. If dublicate number was typed, it will be fixed to the first
free number. Also warning massage and free number will be shown.
Plugin was tested for input deck of MCNP5-1.40 and MCNP5-1.60.
Input deck should include titles of each block:
'Begin Cells' - for cells description;
'Begin Surfaces' - for surfaces description;
'Begin Materials' - for materials description;
'Begin Tallies' - for tallies description;
'Begin Source' - for source and settings description
The order of the blocks should be as in the list above.
Input deck should be open with 'mcnp' syntax
(https://github.com/danyalturkoglu/MCNP-syntax-highlighting).
"""
import sublime
import sublime_plugin
import re

ch2 = None


class CheckNumberListener(sublime_plugin.ViewEventListener):
    @classmethod
    def is_applicable(cls, settings):
        syntax = settings.get('syntax')
        if syntax == 'Packages/User/mcnp.sublime-syntax':
            return True

    def on_modified_async(self):

        global ch2

        def show_phantom_popup(pos, free_numbers, numbers, b_ins="", e_ins=""):
            ''' show phantom and popup meny, insert free number in cur_line,
             clear number list'''
            style = '<style>.w { color: red; \
                                 background-color: #ffff00}</style>'
            ph_content = '<body id="whitespace">' + style + '<span class="w"> \
                        This number is already taken! The first available \
                        number will be inserted. </span></body>'
            v.add_phantom("warning", pos,
                          ph_content, sublime.LAYOUT_INLINE)
            v.show_popup_menu(free_numbers, None)
            v.erase_phantoms("warning")
            v.run_command("move_to",
                          {"to": "bol", "extend": True})
            v.run_command("insert",
                          {'characters': b_ins + free_numbers[0] + e_ins})
            print("Total number: " + str(len(numbers)))
            numbers.clear()

        v = self.view.window().active_view()
        ch1 = v.change_count()
        if ch1 != ch2:
            # get current pos of caret
            cur_pos_row, cur_pos_col = v.rowcol(v.sel()[0].b)
            cur_pos = sublime.Region(v.text_point(cur_pos_row, cur_pos_col),
                                     v.text_point(cur_pos_row, cur_pos_col))
            cur_line = sublime.Region(v.text_point(cur_pos_row, 0),
                                      v.text_point(cur_pos_row, 80))
            # get begin position of cells, surfaces, materials, tallies
            # and Begin Source blocks
            cell_start = v.rowcol(v.find('Begin Cells', 0).b)[0]
            surf_start = v.rowcol(v.find('Begin Surfaces', 0).b)[0]
            mat_start = v.rowcol(v.find('Begin Materials', 0).b)[0]
            tal_start = v.rowcol(v.find('Begin Tallies', 0).b)[0]
            src_start = v.rowcol(v.find('Begin Source', 0).b)[0]
            match_cs = re.search(r'^\d+ ', v.substr(cur_line))
            match_m = re.search(r'^m\d* ', v.substr(cur_line))
            match_t = re.search(r'^f\d*:', v.substr(cur_line))

            # for cell processing
            if (match_cs and cell_start <= cur_pos_row <= surf_start and
                    cur_pos_col <= 9):
                # create a set of cell numbers
                cell_block = sublime.Region(v.text_point(cell_start + 1, 0),
                                            v.text_point(surf_start + 1, 0))
                lines = v.lines(cell_block)
                cells = []
                for line in lines:
                    match1 = re.search(r'^\d+ ', v.substr(line))
                    if match1:
                        cells.append(int(match1.group().rstrip()))
                lines.clear()
                # add phantom if typed cell is in cells
                match_cs_int = int(match_cs.group().rstrip())
                cells.remove(match_cs_int)
                if match_cs_int in cells:
                    # create list of nearest 20 free cell numbers ascending
                    free_cell_numbers = []
                    i = 0
                    while i < 1:
                        if match_cs_int not in cells:
                            free_cell_numbers.append(str(match_cs_int))
                            i += 1
                        match_cs_int = match_cs_int + 1
                    show_phantom_popup(cur_pos, free_cell_numbers, cells,
                                       e_ins=" ")
                else:
                    print("Cell number is free.")

            # for surfaces processing
            elif (match_cs and surf_start <= cur_pos_row <= mat_start and
                  cur_pos_col <= 9):
                # create a set of surfaces numbers
                surf_block = sublime.Region(v.text_point(surf_start + 1, 0),
                                            v.text_point(mat_start + 1, 0))
                lines = v.lines(surf_block)
                surfs = []
                for line in lines:
                    match1 = re.search(r'^\d+ ', v.substr(line))
                    if match1:
                        surfs.append(int(match1.group().rstrip()))
                lines.clear()
                # add phantom if typed surf is in surfs
                match_cs_int = int(match_cs.group().rstrip())
                surfs.remove(match_cs_int)
                if match_cs_int in surfs:
                    # create list of nearest 20 free surf numbers ascending
                    free_surf_numbers = []
                    i = 0
                    while i < 1:
                        if match_cs_int not in surfs:
                            free_surf_numbers.append(str(match_cs_int))
                            i += 1
                        match_cs_int = match_cs_int + 1
                    show_phantom_popup(cur_pos, free_surf_numbers, surfs,
                                       e_ins=" ")
                else:
                    print("Surface number is free.")

            # for material processing   
            elif (match_m and mat_start <= cur_pos_row <= tal_start and
                    cur_pos_col <= 9):
                # create a set of cell numbers
                mat_block = sublime.Region(v.text_point(mat_start + 1, 0),
                                           v.text_point(tal_start + 1, 0))
                lines = v.lines(mat_block)
                materials = []
                for line in lines:
                    match1 = re.search(r'^m\d* ', v.substr(line))
                    if match1:
                        materials.append(int(match1.group().lstrip('m')))
                lines.clear()
                # add phantom if typed material is in materials
                match_m_int = int(match_m.group().lstrip('m'))
                materials.remove(match_m_int)
                if match_m_int in materials:
                    # create list of nearest 15 free material numbers ascending
                    free_mat_numbers = []
                    i = 0
                    while i < 1:
                        if match_m_int not in materials:
                            free_mat_numbers.append(str(match_m_int))
                            i += 1
                        match_m_int = match_m_int + 1
                    show_phantom_popup(cur_pos, free_mat_numbers, materials,
                                       b_ins="m", e_ins=" ")
                else:
                    print("Material number is free.")

            # for tallies processing
            elif match_t and cur_pos_row >= tal_start and cur_pos_col <= 9:
                # create a set of cell numbers
                tal_block = sublime.Region(v.text_point(tal_start + 1, 0),
                                           v.text_point(src_start + 1, 0))
                lines = v.lines(tal_block)
                tallies = []
                for line in lines:
                    match1 = re.search(r'^f\d*:', v.substr(line))
                    if match1:
                        tallies.append(int(match1.group()[1:-1]))
                lines.clear()
                # add phantom if typed tally is in tallies
                match_t_str = match_t.group()[1:-1]
                tallies.remove(int(match_t_str))
                if int(match_t_str) in tallies:
                    # create list of nearest 15 free tally numbers ascending
                    free_tally_numbers = []
                    i = 0
                    while i < 1:
                        if int(match_t_str) not in tallies:
                            free_tally_numbers.append(match_t_str)
                            i += 1
                        match_t_numb = int(match_t_str[:-1])
                        match_t_type = match_t_str[-1]
                        match_t_str = str(match_t_numb + 1) + match_t_type
                    show_phantom_popup(cur_pos, free_tally_numbers, tallies,
                                       b_ins="f", e_ins=":")
                else:
                    print("Tally number is free.")
            else:
                print("Out of search range or nothing was found.")
            ch2 = v.change_count()
