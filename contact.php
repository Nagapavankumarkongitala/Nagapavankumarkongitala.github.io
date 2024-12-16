<?php
    if (isset($_POST["submit"])) {
        $name = strip_tags(trim($_POST['name']));
        $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
        $message = trim($_POST['message']);
        $subject = strip_tags(trim($_POST['subject']));
        $to = 'kumar.knp.82@gmail.com'; 
        $from = 'From: Parax Contact Form <' . $email . '>';

        $body = "From: $name\n E-Mail: $email\n Subject: $subject\n Message:\n $message";

        if (mail($to, $subject, $body, $from)) {
            header("Location: thank-you.html");
            exit;
        } else {
            echo "Error! Please try again.";
        }
    }
?>

?>