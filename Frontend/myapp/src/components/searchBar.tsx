import * as React from "react";
export function Searchbar() {
  return (
    <div>
      <form  className="formsearchbar">
        <input type="text" placeholder="Playstation 5 " className="searchbar"/>
        <button type="submit" className="Sbutton" > <img src="/SBAR.svg" width={13} height={22}></img> </button>
      </form>
    </div>
  );
}
