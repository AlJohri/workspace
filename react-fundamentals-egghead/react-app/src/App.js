import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  static defaultProps = {
    val: 0
  }
  update = () => {
    ReactDOM.render(<App val={this.props.val+1}/>, document.getElementById('root'))
  }
  render() {
    return <button onClick={this.update}>{this.props.val}</button>
  }

}

export default App;
