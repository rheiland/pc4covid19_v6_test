style = """
    <style>
       .jupyter-widgets-output-area .output_scroll {
            height: unset !important;
            border-radius: unset !important;
            -webkit-box-shadow: unset !important;
            box-shadow: unset !important;
        }
        .jupyter-widgets-output-area  {
            height: auto !important;
            width: 100%; !important;
        }
    </style>
    """
%matplotlib inline
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100%;  !important; }</style>"))
display(HTML(style))
import sys, os
sys.path.insert(0, os.path.abspath('bin'))
import pc4covid19
pc4covid19.gui
