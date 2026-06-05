async function generateApp() {
    const prompt = document.getElementById("prompt").value;

    const status = document.getElementById("status");
    const output = document.getElementById("output");
    const steps = document.querySelectorAll(".step");

    // reset UI
    steps.forEach(s => {
        s.classList.remove("active", "done");
    });

    status.innerText = "Processing request...";
    status.classList.add("loading");

    output.innerText = "Thinking...";

    let currentStep = 0;

    function activateStep(index) {
        if (index > 0) {
            steps[index - 1].classList.remove("active");
            steps[index - 1].classList.add("done");
        }
        if (index < steps.length) {
            steps[index].classList.add("active");
        }
    }

    const interval = setInterval(() => {
        if (currentStep < steps.length) {
            activateStep(currentStep);
            currentStep++;
        }
    }, 400);

    try {
        const response = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        const result = data.result;

        clearInterval(interval);

        // finish pipeline animation
        steps.forEach(s => {
            s.classList.remove("active");
            s.classList.add("done");
        });

        status.innerText = "Status: " + result.status;
        status.classList.remove("loading");

        // =========================
        // STREAMING OUTPUT (NEW)
        // =========================
        output.innerText = "";
        typeWriter(JSON.stringify(result, null, 2), output, 6);

    } catch (error) {
        clearInterval(interval);

        status.innerText = "Error connecting backend";
        status.classList.remove("loading");

        output.innerText = error;
    }
}


// =========================
// TYPEWRITER FUNCTION
// =========================
function typeWriter(text, element, speed) {
    let i = 0;

    function write() {
        if (i < text.length) {
            element.innerText += text.charAt(i);
            i++;
            setTimeout(write, speed);
        }
    }

    write();
}