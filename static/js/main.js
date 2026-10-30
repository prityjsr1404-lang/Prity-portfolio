document.addEventListener("DOMContentLoaded", function() {
    // Typing Effect Logic
    const textElement = document.querySelector('.typing-text');
    if (textElement) {
        const text = textElement.getAttribute('data-text');
        textElement.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < text.length) {
                textElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100); // Speed of typing
            }
        }
        
        // Thodi der ruk kar start karega
        setTimeout(typeWriter, 1000); 
    }
});