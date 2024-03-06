export function Card1() {
  const price = 1999;
  return (
    <div className="card1">
      <h1
        style={{
          fontFamily: "Poppins",
          color: "white",
          position: "absolute",
          fontSize: "60px",
          top: "25%",
        }}
      >
        {price}$
      </h1>
      <img
        src="laptop.png"
        width={250}
        height={220}
        style={{
          float: "right",
          textAlign: "right",
          top: "13%",
          position: "absolute",
        }}
      ></img>
      <button
        style={{
          position: "absolute",
          top: "80%",
          left: "12%",
          background: "white",
          borderRadius: "20px",
          //   border: "2px solid yellow",
          width: "120px",
          height: "55px",
        }}
      >
        <h4 style={{ color: "red", fontFamily: "Poppins" }}>Add to cart</h4>
      </button>
      <button
        style={{
          position: "absolute",
          top: "80%",
          left: "32%",
          background: "white",
          borderRadius: "20px",
          width: "120px",
          height: "55px",
        }}
      >
        <h4 style={{ color: "red", fontFamily: "Poppins" }}>More Details</h4>
      </button>
    </div>
  );
}
