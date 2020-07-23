import React, { Component } from "react";
import "./App.css";
import MyForm from "./components/Form";

import axios from "axios";
import Results from "./components/Results";

class App extends Component {
  constructor() {
    super();
    this.state = {
      response: [],
      status: "No results to display",
    };
  }

  handleLoginFormSubmit = (values) => {
    const url = `http://localhost:5001/api?postcode=${values.postcode}&radius=${values.radius}`;
    axios
      .get(url)
      .then((res) => {
        res.status === 200
          ? this.setState({ response: res.data })
          : this.setState({ response: [] });
      })
      .catch((err) => {
        console.log(err);
        this.setState({ status: "No results to display" });
      });
  };

  render() {
    return (
      <div className="App">
        <h1>Store Finder</h1>
        <p>Enter a postcode and radius below to find stores in area:</p>
        <MyForm handleLoginFormSubmit={this.handleLoginFormSubmit} />
        {this.state.response.length > 0 ? (
          <Results results={this.state.response} />
        ) : (
          this.state.status
        )}
      </div>
    );
  }
}

export default App;
