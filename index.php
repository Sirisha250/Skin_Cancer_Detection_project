<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skin Cancer Detection</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Skin Cancer Detection</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <?php if (isset($_SESSION['user_id'])): ?>
                    <li><span>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?></span></li>
                    <li><a href="logout.php">Logout</a></li>
                <?php else: ?>
                    <li><a href="login.php">Login</a></li>
                    <li><a href="signup.html">Sign Up</a></li>
                <?php endif; ?>
                <li><a href="prediction.html">Prediction</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <h2>Welcome to Skin Cancer Detection</h2>
        <p>Our service provides a reliable method to detect skin cancer at an early stage.</p>
        <h3>Meet Our Doctors</h3>
        <div class="doctors">
            <div class="doctor">
                <img src="data:image/jpeg;base64,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" alt="Doctor 1" class="doctor-img">
                <h4>Dr. Smith</h4>
                <p>Dermatologist</p>
            </div>
            <div class="doctor">
                <img src="https://cdn-cpilg.nitrocdn.com/AUXIVIQtsIdjcKgcKxCkSmSPjQBhKiDP/assets/images/optimized/rev-36317f8/www.medicoexperts.com/wp-content/uploads/2021/12/dr-sanjay-sharma-surgical-oncologist.jpg" alt="Doctor 2" class="doctor-img">
                <h4>Dr. Johnson</h4>
                <p>Oncologist</p>
            </div>
            <div class="doctor">
                <img src="https://cdn-cpilg.nitrocdn.com/AUXIVIQtsIdjcKgcKxCkSmSPjQBhKiDP/assets/images/optimized/rev-36317f8/www.medicoexperts.com/wp-content/uploads/2022/01/Dr.-Anil-D-Cruz.jpg" alt="Doctor 3" class="doctor-img">
                <h4>Dr. Lee</h4>
                <p>Skin Cancer Specialist</p>
            </div>
        </div>
    </main>
    
    <footer>
        <p>&copy; 2024 Skin Cancer Detection. All rights reserved.</p>
    </footer>
</body>
</html>
