const fs = require('fs')

module.exports = message => {
	fs.stat(`./Server ${message.guild.id}.txt`, function (err, stat) {
		if (err == null) { //File already exists
			fs.readFile(`./Server ${message.guild.id}.txt`, 'utf-8', function (err, data) {
				if (err) return console.log(err);
				if (data.indexOf(message.author.id) === -1) { //File exists but author is untracked, assume level 0
					message.reply("you are currently level 0, with 0 exp out of 24!")
				} else { //File exists and author is tracked, actually get their rank, level and experience
					//Get user's data
					values = data.substring(data.indexOf(message.author.id) + message.author.id.length + 1)
					values = values.substring(0, values.indexOf("END"))
					level = Number(values.substring(5, values.indexOf(" ")))
					exp_current = Number(values.substring(values.indexOf(" ") + 1, values.indexOf("/"))) + 3
					exp_max = Number(values.substring(values.indexOf("/") + 1))
					//Get other users' data to get a rank
					other = []
					rank = 1
					data = data.replace(data.substring(data.indexOf(message.author.id), data.indexOf("END") + 3)) //Don't compare author's rank to author's rank
					while (data.indexOf("level") !== -1) {
						other.push(data.substring(data.indexOf("level") + 5, data.indexOf("END")))
						data = data.replace(data.substring(data.indexOf("level"), data.indexOf("END") + 3))
					}
					for (i = 0; i < other.length; i++) {
						o_level = Number(other[i].substring(0, other[i].indexOf(" ")))
						if (o_level > level) {
							rank++
						} else if (o_level === level) {
							o_exp = Number(other[i].substring(other[i].indexOf(" ") + 1, other[i].indexOf("/")))
							if (o_exp > exp_current) rank++
						}
					}
					//Send message
					message.reply(`you are currently rank ${rank} at level ${level}, with ${exp_current} exp out of ${exp_max}!`)
				}
			})
		} else if (err.code === 'ENOENT') { //File doesn't exist, assume level 0
			message.reply("you are currently level 0, with 0 exp out of 24!")
		}
	})
}
