import axios from 'axios';

export default class GET {
    calendar() {
        const url = '/Calendar/init';
        return axios.get(url)
    }

    weather() {
        const url = '/Weather/init';
        return axios.get(url)
    }

    weatherCitySearch(query) {
        const url = `/Weather/query=${query}`;
        return axios.get(url, query)
    }
}