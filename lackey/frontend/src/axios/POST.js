import axios from 'axios';

export default class POST {
    calendar() {
        const url = '/api/Calendar';
        return axios.post(url)
    }
}