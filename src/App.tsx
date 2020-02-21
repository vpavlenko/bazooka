import React, { useState } from "react";
import "./App.css";
import { Button } from "antd";
import { LEVELS } from "./levels";

function App() {
  const [level, setLevel] = useState(0);

  return (
    <div>
      <div style={{ position: "fixed" }}>
        <Button
          shape="circle"
          icon="left"
          onClick={() => setLevel(level - 1)}
        />
        {level}
        <Button
          shape="circle"
          icon="right"
          onClick={() => setLevel(level + 1)}
        />
      </div>
      <div
        style={{
          width: "672px",
          marginLeft: "100px",
          fontFamily: "PT serif",
          color: "#000",
          fontSize: '16px',
          marginTop: '3em',
        }}
      >
        <div dangerouslySetInnerHTML={{ __html: LEVELS[level] }} />
      </div>
    </div>
  );
}

export default App;
