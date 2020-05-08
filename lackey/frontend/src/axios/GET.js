import axios from 'axios';

export default class GET {
    calendar() {
        const url = '/api/Calendar';
        return axios.get(url)
    }
}