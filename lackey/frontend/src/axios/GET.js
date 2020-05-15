import axios from 'axios';

export default class GET {
    calendar(action) {
        const url = `/Calendar/${action}`;
        return axios.get(url)
    }

    weather(action) {
        const url = `/Weather/${action}`;
        return axios.get(url, action)
    }

    weatherCitySearch(query) {
        const url = `/Weather/query=${query}`;
        return axios.get(url, query)
    }
}