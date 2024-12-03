# The structure of VENVGEN code

```
                                                                                                                      run.py 
                                                                                                                        │
                                                                                                                    venvgen/
                                                                                                                        │
                                                                                                                  ./venvgen.py
                                                                                                                        │
                                                                      ┌─────────────────────────────────────────────────┴───────────────────────────────────────────────────┐
                                                                      │                                                                                                     │
                                                                  ./utils                                                                                             ./general/
                                                                      │                                                                                                     │
                                                             ./ui_controller.py                                                                                      ./ui_helper.py
                                                                      │                                                                                                     │        
              ┌────────────────────────┬────────────────────────┬─────┴───────────────────┬────────────────────┐                            ┌───────────────────────────────┴
              │                        │                        │                         │                    │                            │
              │                        │                        │                         │                    │                            │
  ./all_system_control.py  ./system_control_protocol.py   ./string_processing.py   ./ANSI_color.py  ./ANSI_line_modification.py    ../utils/system_check.py











```