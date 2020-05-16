import axios from 'axios';

export default class DEL {
    delete(view, id) {
        const url = `/${view}/${id}`;
        return axios.delete(url, id)
    }
}