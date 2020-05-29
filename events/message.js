const online = require('../commands/online')
const kick = require('../commands/kick')
const ban = require('../commands/ban')
const mute = require('../commands/mute')
const warn = require('../commands/warn')
const rank = require('../commands/rank')
const fs = require('fs')
prefix = '-'

function levelling(message) {
	fs.readFile(`./Server ${message.guild.id}.txt`, 'utf-8', function (err, data) {
		if (err) return console.log(err);
		if (data.indexOf(message.author.id) === -1) {
			new_data = data + `${message.author.id} level0 0/24END\n`
			fs.writeFile(`./Server ${message.guild.id}.txt`, new_data, function (err) {
				if (err) return console.log(err);
				console.log(`Now tracking ${message.author.username} on ${message.guild.name}!`)
			})
		} else {
			values = data.substring(data.indexOf(message.author.id) + message.author.id.length + 1)
			values = values.substring(0, values.indexOf("END"))
			level = Number(values.substring(5, values.indexOf(" ")))
			exp_current = Number(values.substring(values.indexOf(" ") + 1, values.indexOf("/"))) + 3
			exp_max = Number(values.substring(values.indexOf("/") + 1))
			if (exp_current >= exp_max) {
				level++
				exp_current = 0
				exp_max = exp_max * 1.5
				message.reply(`you are now level ${level}!`)
			}
			new_values = `level${level} ${exp_current}/${exp_max}`
			data = data.replace(values, new_values)
			fs.writeFile(`./Server ${message.guild.id}.txt`, data, function (err) {
				if (err) return console.log(err);
			})
		}
	})
}

module.exports = (client, message) => {
	if (!message.guild) return

	if (!message.author.bot) {
		fs.stat(`./Server ${message.guild.id}.txt`, function (err, stat) {
			if (err == null) { //File already exists
				levelling(message)
			} else if (err.code === 'ENOENT') { //File doesn't exist, create it
				fs.writeFile(`./Server ${message.guild.id}.txt`, `LEVELLING ON ${message.guild.name} IS TRACKED IN THIS FILE\n\n`, function (err) {
					if (err) return console.log(err);
					console.log(`The "Server ${message.guild.id}.txt" file has been created!`)
					levelling(message)
				})
			} else {
				console.log('ERROR WITH LEVELLING: ', err.code)
			}
		})
	}

	if (message.member.hasPermission('KICK_MEMBERS')) {
		if (message.content.startsWith(`${prefix}kick`)) {
			return kick(message)
		}
		if (message.content.startsWith(`${prefix}mute`)) {
			return mute(message)
		}
		if (message.content.startsWith(`${prefix}warn`)) {
			return warn(message)
		}
	}
	if (message.member.hasPermission('BAN_MEMBERS')) {
		if (message.content.startsWith(`${prefix}ban`)) {
			return ban(message)
		}
	}
	if (message.content.startsWith(`${prefix}online`)) {
		return online(message)
	}
	if (message.content.startsWith(`${prefix}rank`)) {
		return rank(message)
	}
}
