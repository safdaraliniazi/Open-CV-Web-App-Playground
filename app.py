import streamlit as st 
import cv2 
import numpy as np




def main():

    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    st.header('Open-CV Playground')

    activities = ['Drawing' , 'Image Processing']
    choice = st.sidebar.selectbox('Select Activity' , activities)

    # st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # with st.form("my-form", clear_on_submit=True):
    #         img = st.file_uploader("FILE UPLOADER")
    #         submitted = st.form_submit_button()
    
    def draw_line():
         x1 = st.sidebar.slider('Select x1', 0, perma_img.shape[0], 1)
         y1 = st.sidebar.slider('Select y1', 0, perma_img.shape[1], 1)
         x2 = st.sidebar.slider('Select x2', 0, perma_img.shape[0], 1)
         y2 = st.sidebar.slider('Select y2', 0, perma_img.shape[1], 1)
         thickness = st.sidebar.slider('Select line width', 0, 25, 1)
         cv2.line(output , (x1,y1) , (x2,y2) , (0,0,255),thickness)  
         col2.image(output)

    def draw_rectangle():
        x1 = st.sidebar.slider('Select x1', 0, perma_img.shape[0], 1)
        y1 = st.sidebar.slider('Select y1', 0, perma_img.shape[1], 1)
        x2 = st.sidebar.slider('Select x2', 0, perma_img.shape[0], 1)
        y2 = st.sidebar.slider('Select y2', 0, perma_img.shape[1], 1)
        thickness = st.sidebar.slider('Select Rectangle width (-1 to fill)', -1, 25, 1)
        
        cv2.rectangle(output , (x1,y1) , (x2 , y2) , (0,0,255) , thickness)
        col2.image(output)
    
    def draw_circle():
        x1 = st.sidebar.slider('Select Center\'s x1', 0, perma_img.shape[0], 1)
        y1 = st.sidebar.slider('Select Center\'s y1', 0, perma_img.shape[1], 1)
        r = st.sidebar.slider('Select Radius' , 1,100 ,1)
        thickness = st.sidebar.slider('Select Circle\'s width (-1 to fill)', -1, 25, 1)
        cv2.circle(output , (x1,y1) , r , (255,0,0) , thickness)
        col2.image(output)

    def write_text():
         fonts = ['cv2.FONT_HERSHEY_COMPLEX' , 'cv2.FONT_HERSHEY_COMPLEX_SMALL' , 'cv2.FONT_HERSHEY_DUPLEX' , 'cv2.FONT_HERSHEY_PLAIN' , 'cv2.FONT_HERSHEY_SCRIPT_COMPLEX' , 'cv2.FONT_HERSHEY_SCRIPT_SIMPLEX' , 'cv2.FONT_HERSHEY_SIMPLEX' , 'cv2.FONT_HERSHEY_TRIPLEX']
         font_dict = {'cv2.FONT_HERSHEY_COMPLEX': 3  , 'cv2.FONT_HERSHEY_COMPLEX_SMALL' : 5 , 'cv2.FONT_HERSHEY_DUPLEX' : 2 , 'cv2.FONT_HERSHEY_PLAIN' : 1 , 'cv2.FONT_HERSHEY_SCRIPT_COMPLEX' : 7  , 'cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ' : 6 , 'cv2.FONT_HERSHEY_SIMPLEX' : 0  ,'cv2.FONT_HERSHEY_TRIPLEX' : 4}
         text = st.sidebar.text_input('Enter the text')
         font = st.sidebar.selectbox('Select Font' , fonts)
         font_size = st.sidebar.number_input('Enter the font size' , min_value=2)
         x1 = st.sidebar.slider('Select Origin\'s x', 0, perma_img.shape[0], 1)
         y1 = st.sidebar.slider('Select Origin\'s y', 0, perma_img.shape[1], 1)
         cv2.putText(output,text, (x1,y1), font_dict.get(font), font_size ,(0,0,0),2,cv2.LINE_AA)
         col2.image(output)


    def draw_polygon():
         st.sidebar.write('Under Construction :woman-raising-hand:')


    def bgr_2_gray():
         output = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
         output = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
         col1 , col2 = st.columns(2)
         col1.text('Original')
         col2.text('Output')
         col1.image(img)
         col2.image(output)
         

    def bgr_2_hsv():
        output = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
        output = cv2.cvtColor(img , cv2.COLOR_RGB2HSV)
        col1 , col2 = st.columns(2)
        col1.text('Original')
        col2.text('Output')
        col1.image(img)
        col2.image(output)

    def scaling():
     fx = st.sidebar.slider('Enter fx' , 1 , 10 , 1)
     fy = st.sidebar.slider('Enter fy' , 1 , 10 , 1)
     all_interpoltion = [cv2.INTER_AREA , cv2.INTER_BITS , cv2.INTER_BITS2 , cv2.INTER_CUBIC , cv2.INTER_LANCZOS4 , cv2.INTER_LINEAR , cv2.INTER_LINEAR_EXACT , cv2.INTER_MAX , cv2.INTER_TAB_SIZE , cv2.INTER_NEAREST , cv2.INTER_TAB_SIZE2]
     interpolation = st.sidebar.selectbox('Select Interpolation ' , all_interpoltion)
     output = cv2.resize(img,None , fx , fy , interpolation)
     st.image(output)
     
    def translation():
     tx = st.sidebar.slider('Enter tx' , 1 , img.shape[0] , 1)
     ty = st.sidebar.slider('Enter ty' , 1 , img.shape[1] , 1)
     M = np.float32([[1,0,tx],[0,1,ty]])
     output = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
     col1 , col2 = st.columns(2)
     col1.image(img)
     col2.image(output)

    def rotation():
     x = st.sidebar.slider('Rotate about x' , 1 , img.shape[0] , int(img.shape[0] / 2) )
     y = st.sidebar.slider('Rotate about y' , 1 , img.shape[1] , int(img.shape[1] / 2))
     angle = st.sidebar.slider('Rotae about angle' , -360 , 360 , 90)
     M = cv2.getRotationMatrix2D((x,y) , angle , 1)
     output = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
     col1 , col2 = st.columns(2)
     col1.image(img)
     col2.image(output)

    def simple_thresholding():
     img = cv2.imread('sudoku.jpg' , cv2.IMREAD_GRAYSCALE)
     thresh = st.sidebar.slider('The thrash value' , 1 , 255 , 127)
     maxval = st.sidebar.slider('The Max value' , 1 , 255 , 255)
     all_thresh_methods = [cv2.THRESH_BINARY , cv2.THRESH_BINARY_INV , cv2.THRESH_TRUNC , cv2.THRESH_TOZERO , cv2.THRESH_TOZERO_INV]
     thresh_type = st.sidebar.selectbox('Select Thresholding type' , all_thresh_methods)
     ret,output = cv2.threshold(img, thresh, maxval,thresh_type)
     col1 , col2 = st.columns(2)
     col1.image(img)
     col2.image(output)

    def adaptive_thresholding():
     img = cv2.imread('sudoku.jpg' , cv2.IMREAD_GRAYSCALE)
     block_size = st.sidebar.slider('Block Size' , 1 , 99 , 11 , 2)
     maxval = st.sidebar.slider('The Max value' , 1 , 255 , 255)
     all_adaptive_thresh_methods = [cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.ADAPTIVE_THRESH_MEAN_C]
     thresh_type = st.sidebar.selectbox('Select Adaptive Thresholding type' , all_adaptive_thresh_methods)
     output = cv2.adaptiveThreshold(img , maxval , thresh_type , cv2.THRESH_BINARY , block_size, 2)
     col1 , col2 = st.columns(2)
     col1.image(img)
     col2.image(output)

    def canny_edge():
        img = cv2.imread('sudoku.jpg' , cv2.IMREAD_GRAYSCALE)
        threshold1 = st.sidebar.slider('Threshold 1' , 1 , 255 , 100)
        threshold2 = st.sidebar.slider('Threshold 2' , 1 , 255 , 200)
        output = cv2.Canny(img , threshold1 , threshold2)
        col1 , col2 = st.columns(2)
        col1.image(img)
        col2.image(output)


    



    img = cv2.imread('bbl.png')
    perma_img = img
    output = img
    if choice == 'Drawing':
          if img is not None:
            col1 , col2 = st.columns(2)
            col1.text('original Image')
            col1.image(img)
            col2.text('output')

            st.sidebar.header('Choose shape')


            shape = st.sidebar.radio(
                 "Choose Shape" ,
                 ('Line' , 'Rectangle' , 'Circle' , 'Polygon' , 'Adding text to img'),
            )            
            if shape == 'Line':
                 draw_line()
            elif shape == 'Rectangle':
                 draw_rectangle()
            elif shape == 'Circle':
                 draw_circle()
            elif shape == 'Polygon':
                 draw_polygon()
            elif shape == 'Adding text to img':
                 write_text()

    elif choice == 'Image Processing':
         tasks = ['Changing Colorspaces' , 'Geometric Transformations' , 'Image Thresholding' , 'Canny Edge Detection']
         task = st.sidebar.selectbox('Select Task' , tasks)

         if task == 'Changing Colorspaces':
              colorspaces_choices = ['Gray' , 'HSV']
              choice = st.sidebar.selectbox('Select Convsersion' , colorspaces_choices)
              if choice == 'Gray':
                   bgr_2_gray()
              elif choice == 'HSV':
                   bgr_2_hsv() 
         elif task == 'Geometric Transformations':
              geometric_transformations_choices = ['Scaling' , 'Translation' , 'Rotation' , 'Perspective Transformation']
              choice = st.sidebar.selectbox('Select Transformation' , geometric_transformations_choices)

              if choice == 'Scaling':
                   scaling()
              elif choice == 'Translation':
                   translation()
              elif choice == 'Rotation':
                   rotation()
              elif choice == 'Perspective Transformation':
                  st.sidebar.write('Under Construction')
         elif task == 'Image Thresholding':
             Image_thresholding_choices = ['Simple Thresholding' , 'Adaptive Thresholding' , 'Otsu\'s Binarization']
             choice = st.sidebar.selectbox('Select Transformation' , Image_thresholding_choices)

             if choice == 'Simple Thresholding':
                 simple_thresholding()
             elif choice == 'Adaptive Thresholding':
                 adaptive_thresholding()
         elif task == 'Canny Edge Detection':
             canny_edge()
             
                   
                  
              
         


    


if __name__ == '__main__':
    main()