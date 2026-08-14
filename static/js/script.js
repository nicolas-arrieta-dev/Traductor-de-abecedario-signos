document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const fileInput = document.getElementById('fileInput');
    const resultContainer = document.getElementById('resultContainer');
    const originalImage = document.getElementById('originalImage');
    const processedImage = document.getElementById('processedImage');
    const predictedLetter = document.getElementById('predictedLetter');
    
    if (fileInput.files.length === 0) {
        alert('Por favor selecciona una imagen');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        
        originalImage.src = '/' + data.original_image;
        processedImage.src = '/' + data.processed_image;
        predictedLetter.textContent = data.letter;
        resultContainer.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar la imagen');
    });
});