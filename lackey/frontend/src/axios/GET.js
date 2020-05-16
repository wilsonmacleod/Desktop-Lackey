import axios from 'axios';

export default class GET {
    init(view, arg) { // ex. 'Weather', 'init';
        const url = `/${view}/${arg}`;
        return axios.get(url)
    };

    search(view, query) { // ex. 'Weather', 'Honolulu';
        const url = `/${view}/query=${query}`;
        return axios.get(url, query)
    };
}