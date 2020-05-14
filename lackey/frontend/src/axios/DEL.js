import axios from 'axios';

export default class DEL {
    calendar(id) {
        const url = `/Calendar/${id}`;
        return axios.delete(url, id)
    }
}