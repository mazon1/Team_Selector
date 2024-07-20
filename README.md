# ReadME file


# Team Selection App

This is a Streamlit web application that helps in recommending lead roles to team members based on their skill sets. The lead roles include Coding, Documentation & Research, Presentation, and Communication. The app takes user inputs, recommends a role, and saves the data to a CSV file.

## Features

- **Input Form**: Users can enter their name and skill levels in various areas.
- **Recommendation System**: Based on the inputs, the app recommends a lead role.
- **CSV Storage**: User data is saved to a CSV file for future reference.
- **Image Display**: Displays a team-related image for a better user interface.

## Requirements

- Python 3.7 or above
- Streamlit
- Pandas

## Installation

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/team-selection-app.git
    ```
2. Navigate to the project directory.
    ```bash
    cd team-selection-app
    ```
3. Install the required packages.
    ```bash
    pip install streamlit pandas
    ```

## Running the App

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```

## Usage

1. **Enter Your Information**: Fill in your name and skill levels in the form provided.
2. **Get Recommendation**: Click the "Recommend Lead Role" button to get a recommendation.
3. **Save Data**: The input data, along with the recommended role, is saved to a CSV file named `user_data.csv`.

## Code Structure

- **app.py**: The main application file that contains the Streamlit code for the app.
- **teamselectorapp.jpg**: An image file used in the app for visual enhancement.

## Example

1. **Form Inputs**:
    - Name: Anna
    - Project Management: Competent
    - Public Speaking: Expert
    - PPT/Story Development: Proficient
    - Database Management: Competent
    - Coding: Advanced Beginner
    - Deployment: Novice
    - Passion: Project Management

2. **Output**:
    - Recommended Role: Project Management

## License

This project is licensed under the MIT License 

## Acknowledgments

- Inspired by the need for effective team management.
- Built using [Streamlit](https://teamselector.streamlit.app/).

