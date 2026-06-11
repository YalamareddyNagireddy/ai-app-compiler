async function generateApp() {
    const prompt = document.getElementById("prompt").value;

    if (!prompt.trim()) {
        alert("Please enter an app idea");
        return;
    }

    const status = document.getElementById("status");
    const output = document.getElementById("output");
    const steps = document.querySelectorAll(".step");

    // Reset UI
    steps.forEach(step => {
        step.classList.remove("active", "done");
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
        const response = await fetch(
            "https://ai-app-compiler-j6t2.onrender.com/generate",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ prompt })
            }
        );

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        clearInterval(interval);

        // Finish animation
        steps.forEach(step => {
            step.classList.remove("active");
            step.classList.add("done");
        });

        status.innerText = "Generation Complete ✅";
        status.classList.remove("loading");

        output.innerText = "";

        typeWriter(
            JSON.stringify(data.result, null, 2),
            output,
            5
        );

    } catch (error) {
        clearInterval(interval);

        status.innerText = "Backend Connection Failed ❌";
        status.classList.remove("loading");

        output.innerText =
            "Error: " + error.message;
    }
}

// =========================
// TYPEWRITER EFFECT
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