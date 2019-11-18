import matplotlib.pyplot as plt
import numpy as np # dodamo še numerično knjižico 
get_ipython().run_line_magic('matplotlib', 'inline')


def complex_plane2(z,axis_type=0):
    """Creates complex plane and shows complex numbers as vectors (complexors)
    
    Parameters
    ----------
    z : array of complex values
        array of complex values to be shown
    axis_type : int 
        three types of shapes of complex plane:
        0 : symple
        1 : with grid
        2 : moved axis to middle 
    -----------------------------------
    # Example
    z=[20+10j,15,-10-10j,5+15j]
    complex_plane2(z,2) """

    w=max(np.abs(z))
    fig, ax = plt.subplots()
        
    if axis_type==0: 
        plt.axis("off")
        plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
        plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
    elif axis_type==1: 
        plt.axis("on")
        plt.grid()
        plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
        plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
    else:
         # Move left y-axis and bottim x-axis to centre, passing through (0,0)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')

        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        ax.set_xlabel('                                                 Re []')
        ax.set_ylabel('                                                 Im []')

    plt.xlim(-w,w)
    plt.ylim(-w,w)
    plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k');
    plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k');

    for i in range(len(z)):
        fi_a=np.angle(z[i])
        x=z[i].real -abs(w)/20*np.cos(fi_a)
        y=z[i].imag-abs(w)/20*np.sin(fi_a)
        plt.arrow(0, 0, x, y, head_width=w/20, head_length=w/20, fc='b', ec='b');
    plt.show()
        



