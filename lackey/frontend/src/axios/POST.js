import axios from 'axios';

export default class POST {
    calendar(task) {
        const url = `/api/${task}`;
        return axios.post(url, task)
    }
}