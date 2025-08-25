document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const inputs = form.querySelectorAll("input[type='text']");

    form.addEventListener("submit", (e) => {
        let valid = true;

        inputs.forEach(input => {
            const value = parseFloat(input.value);
            if (isNaN(value) || value <= 0) {
                input.style.borderColor = "red";
                valid = false;
            } else {
                input.style.borderColor = "#6c63ff";
            }
        });

        if (!valid) {
            e.preventDefault();
            const msg = form.dataset.invalidMsg;
            alert(msg);
        }
    });

    inputs.forEach((input, index) => {
        input.addEventListener("keydown", (e) => {
            if (e.key === "Enter" && index < inputs.length - 1) {
                e.preventDefault();
                inputs[index + 1].focus();
            }
        });
    });
});