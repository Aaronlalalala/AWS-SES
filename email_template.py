# email_templates.py

EMAIL_SUBJECT = "InstAI-Model-Progress"

EMAIL_BODY_TEXT = """
Dear {name},

I hope this message finds you well.

I am writing to provide you with an update on the progress of our model development at InstaAI. We are excited to share some significant milestones and ongoing efforts to ensure the highest quality and performance of our model.

Current Progress:

1. Development Phase: We have successfully completed the initial development phase and have moved into the advanced testing phase. Our team has implemented key features and improvements based on the feedback we received.
2. Performance Metrics: Preliminary results indicate that the model is performing above our expected benchmarks, particularly in terms of accuracy and processing speed. We are continuously refining our algorithms to enhance these metrics further.
3. Data Integration: Our data integration process has been streamlined, allowing us to utilize a broader dataset for training, which has significantly improved the robustness of our model.

Next Steps:

1. Extended Testing: We will continue with extended testing to ensure the model performs well across a variety of scenarios and use cases.
2. User Feedback: We plan to engage a select group of users for beta testing and feedback. Your insights will be invaluable in refining the final product.
3. Deployment Preparations: Concurrently, we are preparing for a smooth deployment process, ensuring all necessary infrastructure is in place for a seamless transition.

We are committed to keeping you informed throughout this process and greatly appreciate your continued support and patience. Should you have any questions or require further information, please do not hesitate to reach out.

Thank you for your attention and collaboration.

<p>Here's a preview of our InstAI-Web v0.7:</p>
<img src="cid:image" alt="image" style="max-width: 100%;">
Best regards,

Aaron
Software Engineer
InstaAI
"""

EMAIL_BODY_HTML = """
<html>
<body>
<p>Dear {name},</p>

<p>I hope this message finds you well.</p>

<p>I am writing to provide you with an update on the progress of our model development at InstaAI. We are excited to share some significant milestones and ongoing efforts to ensure the highest quality and performance of our model.</p>

<h3>Current Progress:</h3>
<ol>
    <li><strong>Development Phase:</strong> We have successfully completed the initial development phase and have moved into the advanced testing phase. Our team has implemented key features and improvements based on the feedback we received.</li>
    <li><strong>Performance Metrics:</strong> Preliminary results indicate that the model is performing above our expected benchmarks, particularly in terms of accuracy and processing speed. We are continuously refining our algorithms to enhance these metrics further.</li>
    <li><strong>Data Integration:</strong> Our data integration process has been streamlined, allowing us to utilize a broader dataset for training, which has significantly improved the robustness of our model.</li>
</ol>

<h3>Next Steps:</h3>
<ol>
    <li><strong>Extended Testing:</strong> We will continue with extended testing to ensure the model performs well across a variety of scenarios and use cases.</li>
    <li><strong>User Feedback:</strong> We plan to engage a select group of users for beta testing and feedback. Your insights will be invaluable in refining the final product.</li>
    <li><strong>Deployment Preparations:</strong> Concurrently, we are preparing for a smooth deployment process, ensuring all necessary infrastructure is in place for a seamless transition.</li>
</ol>

<p>We are committed to keeping you informed throughout this process and greatly appreciate your continued support and patience. Should you have any questions or require further information, please do not hesitate to reach out.</p>

<p>Thank you for your attention and collaboration.</p>

<p>Best regards,</p>

<p>Aaron<br>
Software Engineer<br>
InstaAI</p>
</body>
</html>
"""