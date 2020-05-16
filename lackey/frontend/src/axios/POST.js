import axios from 'axios';

export default class POST {
    add(view, arg) {
        const url = `/${view}/${arg}`;
        return axios.post(url, arg)
    };
}