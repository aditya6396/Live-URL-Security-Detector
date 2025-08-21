# Real-Time URL Detector
## Overview
The **Real-Time URL Detector** is an AI-powered tool designed to enhance web security by monitoring and detecting malicious or unsafe URLs in real-time from video content. Using Optical Character Recognition (OCR) with Tesseract, the system processes video frames to identify URLs displayed on-screen, highlights them with bounding boxes, and saves the processed output as a video. This tool is ideal for applications like live-stream monitoring, web browsing security, or analyzing screen recordings for potential threats.

Developed as an AI-driven project, it leverages computer vision and text extraction to provide real-time URL detection, making it a valuable tool for cybersecurity professionals and researchers.

## Features
- **Real-Time URL Detection**: Extracts URLs from video frames using OCR with Pytesseract.
- **Visual Highlighting**: Draws green bounding boxes and labels around detected URLs in the video.
- **Video Output**: Saves the processed video with highlighted URLs to a `.mp4` file.
- **Efficient Processing**: Supports frame skipping to optimize performance while maintaining accuracy.
- **Configurable Parameters**: Adjustable scale factor, frame skip rate, and OCR confidence threshold for customization.
- **Scalable Design**: Suitable for integration into larger web security or monitoring systems.

## Technologies Used
- **Programming Language**: Python
- **Computer Vision**: OpenCV (`opencv-python`)
- **OCR**: Pytesseract
- **URL Extraction**: `urlextract`
- **Dependencies**: Listed in `req.txt`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/url-detector.git
   cd url-detector
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r req.txt
   ```
   Ensure `req.txt` contains:
   ```
   opencv-python
   pytesseract
   urlextract
   ```

4. **Install Tesseract OCR**:
   - **Windows**: Download and install Tesseract from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki). Add Tesseract to your system PATH (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`).
   - **Linux**: Install via package manager:
     ```bash
     sudo apt-get install tesseract-ocr
     ```
   - **macOS**: Install via Homebrew:
     ```bash
     brew install tesseract
     ```

5. **Prepare Input Video**:
   - Place your input video (e.g., `video2.webm`) in the project directory.
   - Update the `video_path` variable in `ocr.py` to point to your video file.

6. **Run the Application**:
   ```bash
   python ocr.py
   ```
   - The script processes the video, highlights detected URLs, and saves the output to `processed_video_with_highlighted_urls.mp4`.

## Usage
1. **Run the Script**:
   - Execute `python ocr.py` to process the video specified in `video_path`.
   - The script will:
     - Read video frames.
     - Apply OCR to detect text and extract URLs.
     - Draw green bounding boxes and labels around detected URLs.
     - Display the processed frames (scaled for viewing).
     - Save the output video with highlighted URLs.

2. **View Output**:
   - Check the console for detected URLs printed in real-time.
   - Find the processed video at `processed_video_with_highlighted_urls.mp4` in the project directory.
   - Press `q` while the video is displayed to exit early.

3. **Customize Parameters** (in `ocr.py`):
   - `scale_factor`: Adjusts the display size of the video (default: 0.8).
   - `frame_skip`: Controls how many frames to skip for faster processing (default: 2).
   - `video_path`: Set to your input video file.
   - `output_video_path`: Set the output video file name.

## Project Structure
```
url-detector/
├── video2.webm                # Input video (replace with your video)
├── processed_video_with_highlighted_urls.mp4  # Output video
├── ocr.py                    # Main script for URL detection
├── req.txt                   # Dependencies file
├── README.md                 # Project documentation
```

## How It Works
1. **Video Input**: Loads a video file using OpenCV (`cv2.VideoCapture`).
2. **Frame Processing**:
   - Skips frames (based on `frame_skip`) to optimize performance.
   - Resizes frames (1.5x) for better OCR accuracy.
   - Converts frames to grayscale for OCR processing.
3. **OCR and URL Extraction**:
   - Uses Pytesseract to extract text from frames with a confidence threshold (>10).
   - Applies `urlextract` to identify URLs in the extracted text.
4. **Visualization**:
   - Draws green bounding boxes and labels around detected URLs on the original frame.
   - Resizes frames for display using `scale_factor`.
5. **Output**:
   - Saves the processed video with highlighted URLs using `cv2.VideoWriter`.
   - Prints detected URLs to the console.
   - Displays the processed frames in real-time (optional).

## AI-Powered Web Security
- **Purpose**: Enhances web security by detecting potentially malicious or unsafe URLs in real-time, suitable for monitoring live streams, screen recordings, or browsing sessions.
- **AI Component**: Leverages OCR (Pytesseract) for text detection and `urlextract` for precise URL identification, forming an intelligent pipeline for real-time analysis.
- **Applications**: Can be extended to integrate with URL reputation services or machine learning models to classify URLs as malicious or safe.

## Future Improvements
- Integrate a URL reputation API (e.g., Google Safe Browsing) to classify detected URLs as malicious or safe.
- Add real-time alerts for detected malicious URLs.
- Support additional video formats and live webcam input.
- Enhance OCR accuracy with pre-processing techniques (e.g., thresholding, noise reduction).
- Deploy as a web service for remote video processing.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


## Acknowledgments
- Built as an AI-driven web security tool.
- Thanks to the open-source community for providing libraries like OpenCV, Pytesseract, and `urlextract`.
