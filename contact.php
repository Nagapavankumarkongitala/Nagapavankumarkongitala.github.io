<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST["submit"])) {
            var_dump($_POST); // Debugging line
            
            $name = strip_tags(trim($_POST['name']));
            $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
            $message = trim($_POST['message']);
            $subject = strip_tags(trim($_POST['subject']));
            $to = 'kumar.knp.82@gmail.com'; 
            $headers = "From: Parax Contact Form <$email>\r\nReply-To: $email";

            $body = "From: $name\n E-Mail: $email\n Subject: $subject\n Message:\n $message";

            if (mail($to, $subject, $body, $headers)) {
                header("Location: thank-you.html");
                exit;
            } else {
                echo "Error! Please try again.";
            }
        }
    } else {
        echo "405 Method Not Allowed";
    }
?>
