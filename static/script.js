async function predictPrice() {
    const area = 
        document.getElementById("area").value;

    const response = 
        await fetch("/predict", {
            
            method: "POST",

            headers: {
                "Content-type": 'application/json'
            },

            body: JSON.stringify({
                area: area
            })
        });

    const data = await response.json();

    document.getElementById("result").innerHTML =
        `Approx Price ₹${data.price.toFixed(2)} Lakhs`;
}