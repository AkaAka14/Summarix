async function summarize() {
    const textInput = document.getElementById("textInput").value;
    const fileInput = document.getElementById("fileInput")?.files[0];
    const type = document.getElementById("type").value;
    const size = parseInt(document.getElementById("size").value);
    const resultDiv = document.getElementById("result");
  
    const formData = new FormData();
    formData.append("type", type);
    formData.append("size", size);
  
    if (fileInput) {
      formData.append("file", fileInput);
    } else if (textInput.trim()) {
      formData.append("text", textInput);
    } else {
      resultDiv.innerText = "Please provide input text or a file.";
      return;
    }
  
    resultDiv.innerText = "Summarizing... please wait.";
  
    try {
      const response = await fetch("http://localhost:5000/summarize", {
        method: "POST",
        body: formData,
      });
  
      const data = await response.json();
  
      if (data.summary) {
        resultDiv.innerText = data.summary;
      } else {
        resultDiv.innerText = data.error || "Something went wrong.";
      }
    } catch (error) {
      resultDiv.innerText = "Error: " + error.message;
    }
  }
  