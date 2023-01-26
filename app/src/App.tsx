import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

// const node = useRef<HTMLIFrameElement>(null);

interface StatusData {
  status: string;
}

function App() {
  const [fileUpload, setFileUpload] = useState<any>();

  const post = () => {
    console.log("uploading file: ", fileUpload);
    var data = new FormData();
    data.append("file", fileUpload);

    return fetch("http://127.0.0.1:5000", {
      mode: "no-cors",
      method: "POST",
      body: data,
    })
      .then((response) => response.json()) // Parse the response in JSON
      .then(
        (response) => response as StatusData // Cast the response type to our interface
      );
  };

  const handleChange = (event: any) => {
    const file = event.target.files[0];
    setFileUpload(file);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <input type="file" onChange={handleChange} />
        <button onClick={post}>Upload</button>
      </header>
    </div>
  );
}

export default App;
