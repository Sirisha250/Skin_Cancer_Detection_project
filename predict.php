<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Check if an image was uploaded
    if (isset($_FILES['skin_image']) && $_FILES['skin_image']['error'] == 0) {
        $fileTmpPath = $_FILES['skin_image']['tmp_name'];
        $fileName = $_FILES['skin_image']['name'];
        $uploadFileDir = './uploaded_images/';
        $dest_path = $uploadFileDir . $fileName;

        // Create the upload directory if it doesn't exist
        if (!is_dir($uploadFileDir)) {
            mkdir($uploadFileDir);
        }

        // Move the uploaded file to a designated directory
        if (move_uploaded_file($fileTmpPath, $dest_path)) {
            // Call your Python script here
            $pythonPath = "C:\\Program Files\\Python312\\python.exe"; // Adjust if your Python path is different
            $scriptPath = "C:\\xampp\\htdocs\\skin_cancer_app\\predict.py"; // Path to your predict.py
            $command = escapeshellcmd("C:\\path\\to\\your\\python.exe predict.py $dest_path 2>&1");

            $prediction = shell_exec($command);
            

            // Output the prediction result
            echo "<h2>Prediction Result:</h2>";
            echo "<pre>" . htmlspecialchars($prediction) . "</pre>"; // Use <pre> to format the output nicely
        } else {
            echo "There was an error moving the uploaded file.";
        }
    } else {
        echo "No image uploaded or there was an upload error. Error Code: " . $_FILES['skin_image']['error'];
    }
} else {
    echo "Invalid request method.";
}
?>
