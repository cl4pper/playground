import { ACCEPT_FOLLOWER, CREATE_POST, DELETE_POST, START_FOLLOWING } from "./types"

const initialState = {
	chats: 0,
	followers: 0,
	following: 0,
	posts: 0,
}

const reducer = (state = initialState, action) => {
	switch(action.type) {
		case ACCEPT_FOLLOWER:
			return {
				...state,
				followers: state.followers + 1, // todo: increment operator
			}
		case START_FOLLOWING:
			return {
				...state,
				following: state.following + 1, // todo: increment operator
			}
		case CREATE_POST:
			return {
				...state,
				posts: state.posts + 1, // todo: increment operator
			}
		case DELETE_POST:
			return {
				...state,
				posts: state.posts - 1, // todo: decrement operator
			}
		default:
			return state
	}
}