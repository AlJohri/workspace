import { createStore } from 'redux';
import RootReducer from './reducers';

let store = createStore(RootReducer);

// store.subscribe(function(state)) {
//
// });
