# Tools for maintain MCNP input decks with Sublime Text 3

## check_free_number_MCNP.py 
  This plugin helps you to avoid dublicates of
cell/surface/material/tally number. If dublicate number was typed, it
will be fixed to the first free number. Also warning massage and free
number will be shown.  
  Plugin was tested for input deck of MCNP5-1.40 and MCNP5-1.60.  
Input deck should include titles of each block:
- 'Begin Cells' - for cells description;
- 'Begin Surfaces' - for surfaces description;
- 'Begin Materials' - for materials description;
- 'Begin Tallies' - for tallies description;
- 'Begin Source' - for source and settings description.  
  The order of the blocks should be as in the list above.
  Input deck should be open with 'mcnp' syntax
(https://github.com/danyalturkoglu/MCNP-syntax-highlighting). 
![back](./demonstration/gif/check_cell_number.gif)

## show_card_description.py
- Show surface description when the user's mouse hovers over the surface
number in the cell block.
- Show material description ('$' comment on the first line of material card)
when the user's mouse hovers over the surface number in the cell block. 
- Ignore commented surfaces/materials. If the surface/material was not found, 
a warning message pops up.  
  Plugin work with input deck that has titled and ordered block as above.

## mcnp.sublime-syntax
  Syntax-hightlighting for MCNP input deck in Sublime Text 3
(was taken from https://github.com/danyalturkoglu/MCNP-syntax-highlighting
and improved)  
  Syntax does't yet include all key words from MCNP.

## comment1 and comment2 sublime-macro files
  Macros for comment line with 'c' letter and uncomment line respectively.
  For set hotkeys Ctrl+Shift+C and Ctrl+Shift+X add following content to Preferences --> Key Bindings --> right (User) tab.
  ```
  [
   { "keys": ["ctrl+shift+c"], "command": "run_macro_file", "args": {"file": "Packages/User/comment1.sublime-macro"} },
   { "keys": ["ctrl+shift+x"], "command": "run_macro_file", "args": {"file": "Packages/User/comment2.sublime-macro"} }
  ]
  ```
 

