import { TAGS_VIEW } from "@/constant";
import { getItem, setItem } from "@/utils/storage";

export default {
	namespaced: true,
	state: () => ({
		sidebarOpened: true,
		tagsViewList: getItem(TAGS_VIEW) || []
	}),
	mutations: {
		triggerSidebarOpened(state) {
			state.sidebarOpened = !state.sidebarOpened;
		},
		/**
     * 添加 tags
     */
		addTagsViewList(state, tag) {
			const isFind = state.tagsViewList.find(item => {
				return item.path === tag.path;
			});
			// 处理重复
			if (!isFind) {
				state.tagsViewList.push(tag);
				setItem(TAGS_VIEW, state.tagsViewList);
			}
		},
		/**
     * 删除 tag
     * @param {type: 'other'||'right'||'index', index: index} payload
     */
		removeTagsView(state, payload) {
			if (payload.type === "index") {
				state.tagsViewList.splice(payload.index, 1);
			} else if (payload.type === "other") {
				state.tagsViewList.splice(
					payload.index + 1,
					state.tagsViewList.length - payload.index + 1
				);
				state.tagsViewList.splice(0, payload.index);
				if (payload.index != 0) {
					// list第一位加入删除了的首页tag
					state.tagsViewList.unshift({
						fullPath: "/home",
						meta: { title: "首页", affix: true },
						name: "home",
						params: {},
						path: "/home",
						query: {},
						title: "首页"
					});
				}
			} else if (payload.type === "right") {
				state.tagsViewList.splice(
					payload.index + 1,
					state.tagsViewList.length - payload.index + 1
				);
			} else if (payload.type === "all") {
				state.tagsViewList = [];
			}
			setItem(TAGS_VIEW, state.tagsViewList);
		}

	}
};