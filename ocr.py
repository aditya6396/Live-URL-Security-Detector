import cv2
import pytesseract
from urlextract import URLExtract
from pytesseract import Output

# Path to the uploaded video
video_path = 'video2.webm'  # Replace with your video path

# Initialize URL extractor
extractor = URLExtract()

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video was successfully opened
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties (width, height, frames per second)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the output video writer (save the processed video)
output_video_path = 'processed_video_with_highlighted_urls.mp4'  # Output video path
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Video codec for .mp4 format
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Define the scale factor for resizing the displayed frame
scale_factor = 0.8  # 50% of original size

# Process every nth frame
frame_skip = 2  # Change this to skip more frames (e.g., 3, 5 for faster but less precise processing)

# Frame count tracker
frame_count = 0

# Loop through video frames
while True:
    ret, frame = cap.read()

    if not ret:
        break  # End of video

    # Skip frames
    if frame_count % frame_skip != 0:
        frame_count += 1
        continue

    # Resize frame for OCR (improves accuracy)
    scaled_frame = cv2.resize(frame, None, fx=1.5, fy=1.5)

    # Convert to grayscale for OCR
    gray_frame = cv2.cvtColor(scaled_frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the frame
    d = pytesseract.image_to_data(gray_frame, output_type=Output.DICT)
    n_boxes = len(d['text'])

    detected_urls = []

    for i in range(n_boxes):
        if int(d['conf'][i]) > 10:  # Confidence threshold
            text = d['text'][i]
            urls = extractor.find_urls(text)
            if urls:
                detected_urls.extend(urls)

                # Calculate bounding box for the text containing URLs
                (x, y, w, h) = (
                    int(d['left'][i] / 1.5),
                    int(d['top'][i] / 1.5),
                    int(d['width'][i] / 1.5),
                    int(d['height'][i] / 1.5),
                )

                # Draw a rectangle around the detected URL
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Optionally: Label the rectangle with the URL
                cv2.putText(
                    frame,
                    urls[0],
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )

    # Resize frame for display
    small_frame = cv2.resize(frame, (int(frame_width * scale_factor), int(frame_height * scale_factor)))

    # Write the frame to the output video
    out.write(frame)

    # Optionally display the frame
    cv2.imshow('Frame with URLs and Time', small_frame)

    # Print detected URLs
    if detected_urls:
        print("Detected URLs:", detected_urls)

    # Break loop on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved at: {output_video_path}")