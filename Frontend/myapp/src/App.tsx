import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { Searchbar } from "./components/Searchbar.1";
import { Profilebar } from "./components/Profilebar";
import { Cards } from "./components/Cards";
import { Card1 } from "./components/Card1";
import { Card2 } from "./components/Card2";
import { Card3 } from "./components/Card3";
import { Card4 } from "./components/Card4";
function App() {
  const innerWidth = window.innerWidth;
  const innerHeight = window.innerHeight;
  return (
    <>
      <div className="mylogo">
        <img src="/mylogo.png" className="mylogo"></img>
      </div>

      <Searchbar></Searchbar>

      <Profilebar></Profilebar>
      <Cards></Cards>
      <Card1></Card1>
      <Card2></Card2>
      <Card3></Card3>
      <Card4></Card4>
      <div className="welcome">
        Welcome to Shop<span>Easy</span>
      </div>
    </>
  );
}
export default App;
