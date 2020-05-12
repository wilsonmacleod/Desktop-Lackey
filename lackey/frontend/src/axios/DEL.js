import axios from 'axios';

export default class DEL {
    calendar(taskID) {
        const url = `/api/${taskID}`;
        return axios.delete(url, taskID)
    }
}