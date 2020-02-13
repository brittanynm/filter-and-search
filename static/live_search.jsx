
class CustomerSearch extends React.Component {
    constructor() {
        super();
        this.state = {
            customers: {},
            inputValue: '',
            companies: {},
            dropdownValue: '',
            sortSelection: ''
        };
        this.handleSearchChange = this.handleSearchChange.bind(this);
    }

    componentDidMount() {
        $.get('/live_search', {name: ''}, (data) => {
            this.setState({ customers: data });
        });
        $.get('/companies', (data) => {
            this.setState( {companies: data });
        });
    }

    handleSortChange(evt) {
        this.setState({ sortSelection: evt.target.value });
        $.get('/live_search', {name:this.state.inputValue, company:this.state.dropdownValue, sort:evt.target.value}, (data) => {
            this.setState({ customers: data });
        });

    }

    handleSearchChange(evt) {
        var name = ''
        var company = ''
        if (evt.target.id == "dropdown") {
            this.setState({ dropdownValue: evt.target.value });
            company = evt.target.value
            name = this.state.inputValue
        }
        else {
            this.setState({ inputValue: evt.target.value });
            name = evt.target.value
            company = this.state.dropdownValue
        }
        
        $.get('/live_search', {name:name, company:company, sort:this.state.sortSelection}, (data) => {
            this.setState({ customers: data });
        });
    }

    renderCustomers() {
        const customerDivs = [];

        for (const [key, customer] of Object.entries(this.state.customers)) {
            customerDivs.push(
                <div className="customer_fn_ln" key={key}>
                    {customer.first_name} {customer.last_name}, {customer.company_name}<hr />
                </div>
            );
        }

        return customerDivs;
    }

    renderCompanies() {
        const companyDivs = [];

        for (const [key, company] of Object.entries(this.state.companies)) {
            companyDivs.push(
                <option value={key}> {company} </option>);
        }
        return companyDivs;
    }
    
    submitHandler(evt) {
        evt.preventDefault();
    }

    render() {
        return (
            <div className="container-fluid">
                <form 
                    className="form-inline">
                    <div className="form-group">
                        <label id="search-title" htmlFor="name"><h2>Customer Search</h2>
                        </label>Search by first or last name  
                        <input 
                            type="text"
                            className="form-control"
                            id="name"
                            value={this.state.name}
                            onChange={this.handleSearchChange}
                        />
                    </div>
                    <div className="form-group">
                        <label id="search-dropdown" htmlFor="name">
                        </label>Filter by company  
                        <select id="dropdown" onChange={this.handleSearchChange}>
                            <option value=''> Select All</option>
                            {this.renderCompanies()} </select>
                    </div>
                    // <div className="form-group">
                    //     <label id="sort" htmlFor="name">
                    //     </label>Sort results
                    //     <select id="sort" onChange={this.handleSearchChange}>
                    //         <option value="first_name_asc">First Name Ascending</option>
                    //         <option value="first_name_desc">First Name Descending</option>
                    //         <option value="last_name_asc">Last Name Ascending</option>
                    //         <option value="last_name_desc">Last Name Descending</option>

                    //     </select>
                    // </div>
                </form><br /><br />
                
                <form className="form-inline-2">
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