
class CustomerSearch extends React.Component {
    constructor() {
        super();
        this.state = {
            customers: {},
            inputValue: ''
        };
        this.handleSearchChange = this.handleSearchChange.bind(this);
    }

    componentDidMount() {
        $.get('/live_search', {query: ''}, (data) => {
            this.setState({ customers: data });
        });
    }

    handleSearchChange(evt) {
        this.setState({ inputValue: evt.target.value });

        $.get('/live_search', {query: evt.target.value}, (data) => {
            this.setState({ customers: data });
        });
    }

    renderCustomers() {
        const customerDivs = [];

        for (const [key, customer] of Object.entries(this.state.customers)) {
            customerDivs.push(
                <div className="customer_fn_ln" key={key}>
                    {customer.first_name} {customer.last_name}<hr />
                </div>
            );
        }

        return customerDivs;
    }
    
    submitHandler(evt) {
        evt.preventDefault();
    }

    render() {
        return (
            <div className="container-fluid">
                <form 
                    onSubmit={this.submitHandler} 
                    className="form-inline" 
                    method = "GET" 
                    action="/search">
                    <div className="form-group">
                        <label id="search-title" htmlFor="query"><h2>Customer Search</h2>
                        </label>Search by first or last name  
                        <input 
                            type="text"
                            className="form-control"
                            id="query"
                            value={this.state.query}
                            onChange={this.handleSearchChange}
                        />
                    </div>
                </form><br /><br />
                    
                <form className="form-inline-2" method = "GET" action="/">
                    <div className="list" id="customer_list"> <h3>Results</h3>
                        {this.renderCustomers()}
                    </div>
                </form>
                        
            </div>
        );
    }
}

ReactDOM.render(
    <CustomerSearch />, 
    $('#root')[0]
);