
const search = document.getElementById('query');

search.addEventListener('input', response);

async function response(evt) {
    const search = document.getElementById('query');
    console.log(search.value);
    const result = await fetch(`/live_search?query=${search.value}`);
    const data = await result.json();
    console.log("**", data);

    Object.keys(data).forEach(key => {
        let obj = data[key]
        let first_name = obj.first_name
        let last_name = obj.last_name
        let customer_id = obj.customer_id
        let customer_list = document.getElementById("customer_list");
        let display = `<div class="list" id="customer"><div class="customer-name">${first_name}<br>${last_name}<br></div></div>`;
        $('#customer_list').html(display);

    })
}

