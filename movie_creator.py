import cv2


# Open a video capture object 
cap = cv2.VideoCapture(0) 

# Define the codec and create a VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*"XVID") 
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480)) 

# Capture video frames and write them to the file 
while cap.isOpened(): 
    ret, frame = cap.read() 
    if ret: 

      # Flip the frame horizontally 
      frame = cv2.flip(frame, 1) 

      # Write the frame to the output file 
      out.write(frame) 

      # Display the resulting frame 
      cv2.imshow("frame", frame) 

      # Exit if the user presses the ‘q’ key 
      if cv2.waitKey(1) & 0xFF == ord("q"): 
          break 
    else: 
      break 
      
# Release the resources 
cap.release() 
out.release() 
cv2.destroyAllWindows()