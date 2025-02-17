// PREVIEW

const inputElement = document.getElementById('id_image');
const previewElement = document.getElementById('preview');
const cropModal = document.getElementById('cut');
const closeModal = document.getElementById('closeModal');
const modalContent = document.querySelector('.modal-content');
const imageToCrop = document.getElementById('imageToCrop');
const cropButton = document.getElementById('cropButton');

let cropper;

let isMousePressedInside = false;

previewElement.addEventListener('click', function () {
    inputElement.click();
});

inputElement.addEventListener('click', function () {
    inputElement.value = '';
});

inputElement.addEventListener('change', function () {
    if (inputElement.files && inputElement.files[0]) {
        const file = inputElement.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                
                imageToCrop.src = e.target.result;
                cropModal.style.display = 'flex';

                if (cropper) {
                    cropper.destroy();
                    cropper = null;
                }

                    cropper = new Cropper(imageToCrop, {
                        aspectRatio: 1,
                        viewMode: 1,
                        minCropBoxWidth: 100,
                        minCropBoxHeight: 100,
                        cropBoxResizable: true,
                        zoomable: false,
                        responsive: false,
                        scalable: false,
                        ready: function() {
                            const imageData = cropper.getImageData();
                            
                            const cropBoxSize = Math.min(imageData.width, imageData.height);
                            const left = (imageData.width - cropBoxSize) / 2;
                            const top = (imageData.height - cropBoxSize) / 2;
                    
                            cropper.setCropBoxData({
                                left: imageData.left + left,
                                top: imageData.top + top,
                                width: cropBoxSize,
                                height: cropBoxSize
                            });
                        }
                    });
            };

            reader.readAsDataURL(file);
        }
    }
});


cropButton.addEventListener('click', function () {
    if (cropper) {
        const canvas = cropper.getCroppedCanvas({
            width: 300,
            height: 300,
    });

    canvas.toBlob(function (blob) {
        const url = URL.createObjectURL(blob);
        previewElement.src = url;

        cropModal.style.display = 'none';

        const file = new File([blob], inputElement.files[0].name, { type: 'image/jpeg' });
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        inputElement.files = dataTransfer.files;
    });
}
});

closeModal.addEventListener('click', function () {
    cropModal.style.display = 'none';

    if (cropper) {
        cropper.destroy();
        cropper = null;
    }
});

modalContent.addEventListener('mousedown', function () {
    isMousePressedInside = true;
});

window.addEventListener('mouseup', function (event) {
    if (isMousePressedInside) {
        isMousePressedInside = false;
    } else if (event.target === cropModal) {
        cropModal.style.display = 'none';
        if (cropper) {
            cropper.destroy();
            cropper = null;
        }
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll('input');

    inputs.forEach(function(input) {
        if (input.value.trim() !== '') {
            input.classList.add('filled');
        }

        input.addEventListener('input', function() {
            if (this.value.trim() !== '') {
                this.classList.add('filled');
            } else {
                this.classList.remove('filled');
            }
        });
    });
});